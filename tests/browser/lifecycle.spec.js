import {test,expect} from '@playwright/test';
import fs from 'node:fs/promises';
import path from 'node:path';
import {spawnSync} from 'node:child_process';

const original=JSON.parse(await fs.readFile(new URL('../fixtures/reader-original.json',import.meta.url),'utf8'));
const fixture=(entry='0',scale='town',participation='0.025',wage='56000')=>original.cases.find(r=>r.args.join('|')===[entry,scale,participation,wage].join('|')).result;
const held="self.onmessage=({data})=>{if(data.type==='init')self.postMessage({type:'ready',generation:data.generation});};";
const latest=page=>page.evaluate(()=>window.__workers.at(-1).sent.filter(m=>m.type==='evaluate').at(-1));
async function evaluated(page){await expect(page.locator('#export')).toBeEnabled();await expect(page.locator('#lenses .lens')).toHaveCount(3);}
async function exported(page,output){
 const pending=page.waitForEvent('download');await page.locator('#export').click();const download=await pending;
 expect(download.suggestedFilename()).toBe('ceres-draft-evaluation.json');
 if(output)await download.saveAs(output);
 return JSON.parse(await fs.readFile(await download.path(),'utf8'));
}
async function firstWorker(page,body){let count=0;await page.route('**/worker.js',route=>count++===0?route.fulfill({contentType:'text/javascript',body}):route.continue());}
async function stopped(page){await expect.poll(()=>page.workers().length).toBe(0);await expect(page.locator('#export')).toBeDisabled();await expect(page.locator('#lenses .lens')).toHaveCount(0);await expect(page.locator('#retry')).toBeEnabled();}
async function instrument(page){
 await page.addInitScript(()=>{
  const Native=window.Worker;window.__workers=[];window.__ctorAttempted=false;
  window.Worker=class extends Native{
   constructor(...args){
    if(location.search.includes('faultCtor=1')&&!window.__ctorAttempted){window.__ctorAttempted=true;throw new Error('Controlled constructor failure');}
    super(...args);this.sent=[];this.closed=0;window.__workers.push(this);
   }
   postMessage(message,...rest){this.sent.push(structuredClone(message));return super.postMessage(message,...rest);}
   terminate(){this.closed++;return super.terminate();}
  };
 });
}

for(const[name,viewport]of [['desktop',{width:1280,height:900}],['mobile',{width:390,height:844}]]){
 test.describe(name,()=>{
  test.beforeEach(async({page})=>{await page.setViewportSize(viewport);await instrument(page);});

  test('all120 original native outcomes export with their actual UI inputs',async({page},info)=>{
   test.setTimeout(180000);await page.goto('/CERES/');await evaluated(page);
   for(let i=0;i<original.cases.length;i++){
    const row=original.cases[i];const[entry,scale,participation,wage]=row.args;
    const values={entry,scale,participation:String(Number(participation)*100),wage};
    const cleared=await page.evaluate(values=>{
     for(const[id,value]of Object.entries(values))document.getElementById(id).value=value;
     for(const id of ['entry','scale'])document.getElementById(id).dispatchEvent(new Event('change'));
     for(const id of ['participation','wage'])document.getElementById(id).dispatchEvent(new Event('input'));
     return document.getElementById('export').disabled&&document.querySelectorAll('#lenses .lens').length===0;
    },values);expect(cleared).toBe(true);await evaluated(page);
    const data=await exported(page,info.outputPath(`evaluation-${i}.json`));
    expect(data.inputs).toEqual(values);expect(data.result).toEqual(row.result);
    expect(data.source_commit).toBe(await page.locator('#source-revision').textContent());
   }
   await page.screenshot({path:info.outputPath('own-input.png'),fullPage:true});
   expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
  });

  test('cancel during boot terminates then retries with retained assumptions',async({page})=>{
   await firstWorker(page,'self.onmessage=()=>{};');await page.goto('/CERES/?entry=1&scale=village&participation=10&wage=62000');
   await expect(page.locator('#cancel')).toBeEnabled();await expect(page.locator('#wage')).toBeEnabled();
   await page.locator('#cancel').click();await stopped(page);
   expect(await page.evaluate(()=>window.__workers[0].closed)).toBe(1);
   await expect(page.locator('#wage')).toHaveValue('62000');await page.locator('#retry').click();await evaluated(page);
   expect((await exported(page)).result).toEqual(fixture('1','village','0.1','62000'));
  });

  test('cancel during compute terminates the actual worker and recovers',async({page})=>{
   await firstWorker(page,held);await page.goto('/CERES/');await expect(page.locator('#status')).toHaveText('Evaluating…');
   await page.locator('#cancel').click();await stopped(page);expect(await page.evaluate(()=>window.__workers[0].closed)).toBe(1);
   await page.locator('#retry').click();await evaluated(page);expect((await exported(page)).result).toEqual(fixture());
  });

  test('an edit terminates in-flight work and fences its old callback',async({page})=>{
   await firstWorker(page,held);await page.goto('/CERES/');await expect(page.locator('#status')).toHaveText('Evaluating…');
   await page.evaluate(()=>{window.__lateCallback=window.__workers[0].onmessage;const wage=document.getElementById('wage');wage.value='62000';wage.dispatchEvent(new Event('input'));});
   await evaluated(page);expect(await page.evaluate(()=>window.__workers[0].closed)).toBe(1);
   await page.evaluate(wrong=>{
    const request=window.__workers.at(-1).sent.filter(m=>m.type==='evaluate').at(-1);
    window.__lateCallback({data:{type:'result',generation:request.generation,id:request.id,result:wrong,ms:1}});
   },fixture('1','small_city','0.2','200000'));
   const data=await exported(page);expect(data.inputs.wage).toBe('62000');expect(data.result).toEqual(fixture('0','town','0.025','62000'));
  });

  test('wrong IDs/generations, duplicate ready/results and unknown packets cannot replace a result',async({page})=>{
   await firstWorker(page,held);await page.goto('/CERES/');await expect(page.locator('#status')).toHaveText('Evaluating…');
   await page.evaluate(result=>{
    const worker=window.__workers.at(-1),request=worker.sent.filter(m=>m.type==='evaluate').at(-1);
    for(const data of [null,{...request,type:'other'},
     {type:'ready',generation:request.generation},
     {type:'result',generation:request.generation+1,id:request.id,result,ms:1},
     {type:'result',generation:request.generation,id:request.id+1,result,ms:1},
     {type:'error',generation:request.generation,id:request.id+1,message:'stale'}])worker.onmessage({data});
   },fixture('1','village','0.2','10000'));
   await expect(page.locator('#export')).toBeDisabled();expect((await latest(page)).type).toBe('evaluate');
   await page.evaluate(result=>{const w=window.__workers.at(-1),r=w.sent.filter(m=>m.type==='evaluate').at(-1);w.onmessage({data:{type:'result',generation:r.generation,id:r.id,result,ms:1}});},fixture());
   await evaluated(page);
   await page.evaluate(result=>{const w=window.__workers.at(-1),r=w.sent.filter(m=>m.type==='evaluate').at(-1);w.onmessage({data:{type:'result',generation:r.generation,id:r.id,result,ms:1}});},fixture('1','village','0.2','10000'));
   expect((await exported(page)).result).toEqual(fixture());
  });

  for(const phase of ['boot','compute'])test(`${phase} 15-second deadline terminates and allows actual-WASM retry`,async({page})=>{
   await page.clock.install();await firstWorker(page,phase==='boot'?'self.onmessage=()=>{};':held);await page.goto('/CERES/');
   await expect(page.locator('#status')).toContainText(phase==='boot'?'Loading':'Evaluating');
   await page.clock.fastForward(15001);await expect(page.locator('#status')).toContainText('15-second deadline');await stopped(page);
   expect(await page.evaluate(()=>window.__workers[0].closed)).toBe(1);await page.locator('#retry').click();await evaluated(page);
   expect((await exported(page)).result).toEqual(fixture());
  });

  test('actual WASM failure preserves editable assumptions and retries',async({page},info)=>{
   let broken=true;await page.route('**/*.wasm',route=>broken?route.fulfill({status:503,body:'unavailable'}):route.continue());
   await page.goto('/CERES/');await expect(page.locator('#status')).toContainText('could not load');await stopped(page);
   await page.locator('#entry').selectOption('1');await page.locator('#scale').selectOption('village');
   await page.locator('#participation').evaluate(e=>{e.value='20';e.dispatchEvent(new Event('input'));});
   await expect(page.locator('#source-download')).toHaveAttribute('href','downloads/ceres-source.zip');
   await page.screenshot({path:info.outputPath('failed-engine.png'),fullPage:true});
   broken=false;await page.locator('#retry').click();await evaluated(page);expect((await exported(page)).result).toEqual(fixture('1','village','0.2','56000'));
  });

  test('malformed current results stop the worker and never become exports',async({page})=>{
   await firstWorker(page,held);await page.goto('/CERES/');await expect(page.locator('#status')).toHaveText('Evaluating…');
   await page.evaluate(()=>{const w=window.__workers[0],r=w.sent.filter(m=>m.type==='evaluate').at(-1);w.onmessage({data:{type:'result',generation:r.generation,id:r.id,result:{},ms:1}});});
   await expect(page.locator('#status')).toContainText('invalid result');await stopped(page);await page.locator('#retry').click();await evaluated(page);
  });

  test('message decoding errors terminate and recover',async({page})=>{
   await firstWorker(page,held);await page.goto('/CERES/');await expect(page.locator('#status')).toHaveText('Evaluating…');
   await page.evaluate(()=>window.__workers[0].dispatchEvent(new Event('messageerror')));
   await expect(page.locator('#status')).toContainText('unreadable message');await stopped(page);await page.locator('#retry').click();await evaluated(page);
  });

  test('constructor failure offers retry without a page exception',async({page})=>{
   const errors=[];page.on('pageerror',e=>errors.push(e.message));await page.goto('/CERES/?faultCtor=1');
   await expect(page.locator('#status')).toContainText('could not load');await stopped(page);
   await page.locator('#retry').click();await evaluated(page);expect(errors).toEqual([]);
  });

  test('rapid edits clear old output and export only the latest snapshot',async({page})=>{
   await page.goto('/CERES/');await evaluated(page);
   const cleared=await page.evaluate(()=>{
    const p=document.getElementById('participation');
    for(let i=1;i<=20;i++){p.value=String(i);p.dispatchEvent(new Event('input'));}
    document.getElementById('entry').value='1';document.getElementById('scale').value='village';document.getElementById('wage').value='10000';
    for(const id of ['entry','scale'])document.getElementById(id).dispatchEvent(new Event('change'));
    document.getElementById('wage').dispatchEvent(new Event('input'));
    return document.getElementById('export').disabled&&document.querySelectorAll('#lenses .lens').length===0;
   });expect(cleared).toBe(true);await evaluated(page);const data=await exported(page);
   expect(data.inputs).toEqual({entry:'1',scale:'village',participation:'20',wage:'10000'});expect(data.result).toEqual(fixture('1','village','0.2','10000'));
  });

  test('reset during computation terminates and evaluates the original defaults',async({page})=>{
   await firstWorker(page,held);await page.goto('/CERES/?entry=1&scale=village&participation=20&wage=200000');await expect(page.locator('#status')).toHaveText('Evaluating…');
   await page.locator('#reset').click();await evaluated(page);expect(await page.evaluate(()=>window.__workers[0].closed)).toBe(1);
   expect(new URL(page.url()).search).toBe('');const data=await exported(page);
   expect(data.inputs).toEqual({entry:'0',scale:'town',participation:'2.5',wage:'56000'});expect(data.result).toEqual(fixture());
  });

  test('keyboard own input matches native Rust and shares/reloads the same assumptions',async({page})=>{
   await page.goto('/CERES/');await evaluated(page);await page.locator('#participation').focus();await page.keyboard.press('ArrowRight');
   await expect(page.locator('#participation')).toHaveValue('2.6');await evaluated(page);
   const control=path.resolve(process.env.CARGO_TARGET_DIR??'target','debug/examples/reader-control'+(process.platform==='win32'?'.exe':''));
   const submitted=await latest(page);
   const native=spawnSync(control,[String(submitted.entry),submitted.scale,String(submitted.participation),String(submitted.wage)],{encoding:'utf8',timeout:15000});expect(native.status,native.stderr).toBe(0);
   const result=JSON.parse(JSON.parse(native.stdout).json);let data=await exported(page);expect(data.inputs.participation).toBe('2.6');expect(data.result).toEqual(result);
   await page.locator('#share').click();await expect(page.locator('#share-status')).toContainText('address bar');await page.reload();await evaluated(page);
   data=await exported(page);expect(data.inputs.participation).toBe('2.6');expect(data.result).toEqual(result);
  });

  test('an unannounced control edit cannot relabel an already completed export',async({page})=>{
   await page.goto('/CERES/');await evaluated(page);let downloads=0;page.on('download',()=>downloads++);
   await page.locator('#wage').evaluate(e=>{e.value='62000';});await page.locator('#export').click();
   expect(downloads).toBe(0);await evaluated(page);const data=await exported(page);
   expect(data.inputs.wage).toBe('62000');expect(data.result).toEqual(fixture('0','town','0.025','62000'));
  });
 });
}
