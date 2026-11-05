const $=selector=>document.querySelector(selector);
const SOURCE_COMMIT='__SOURCE_COMMIT__';
const DEADLINE_MS=15000;
const fields=['entry','scale','participation','wage'];
const paths=['001-backyard-propane-compact.md','002-induction-modular-small-repair.md'];
let worker=null,generation=0,sequence=0,ready=false,active=null,completed=null;
let bootTimer,computeTimer,debounce;

const inputs=()=>Object.fromEntries(fields.map(id=>[id,$(`#${id}`).value]));
function busy(value){
 $('#results').setAttribute('aria-busy',String(value));
 $('#cancel').disabled=!value;
 $('#retry').disabled=worker!==null;
}
function invalidate(){
 completed=null;$('#export').disabled=true;
 $('#lenses').replaceChildren();$('#population').textContent='';
}
function stop(){
 clearTimeout(bootTimer);clearTimeout(computeTimer);clearTimeout(debounce);
 worker?.terminate();worker=null;ready=false;active=null;generation++;
 busy(false);
}
function fail(message){stop();invalidate();$('#status').textContent=message;}
function labels(){
 $('#participation-value').textContent=`${Number($('#participation').value).toFixed(1)}%`;
 $('#wage-value').textContent=`$${Number($('#wage').value).toLocaleString('en-US')}`;
 $('#catalog-link').href=`https://github.com/giodl73-repo/CERES/blob/${SOURCE_COMMIT}/catalog/smithing/entries/${paths[Number($('#entry').value)]}`;
}
function validResult(result){
 return result&&typeof result==='object'&&typeof result.status==='string'
  &&Number.isFinite(result.population)&&Number.isFinite(result.households)
  &&['market','coop','civic'].every(key=>result[key]&&Number.isFinite(result[key].primary_metric)
    &&typeof result[key].verdict==='string'&&typeof result[key].notes==='string');
}
function display(result){
$('#lenses').replaceChildren();for(const [key,name,label]of [['market','Market','years to recover capital'],['coop','Co-op','break-even members'],['civic','Civic','annual cost per household']]){const lens=result[key],section=document.createElement('article');section.className='lens';section.id=key;const title=document.createElement('h3');title.textContent=name;const verdict=document.createElement('span');verdict.className='badge';verdict.textContent=lens.verdict;title.append(verdict);const metric=document.createElement('strong');metric.textContent=lens.primary_metric<0?'Not recoverable':key==='civic'?`$${lens.primary_metric.toFixed(2)}`:lens.primary_metric.toLocaleString('en-US',{maximumFractionDigits:2});const explanation=document.createElement('p');explanation.textContent=label;const notes=document.createElement('p');notes.textContent=lens.notes.replaceAll('feasible_pool=','Potential members: ').replaceAll('break_even=','break-even members: ').replaceAll('total_annual_cost=','annual cost: $').replaceAll('per_hh=','Annual cost per household: $').replaceAll('threshold=','threshold: ').replaceAll('hrs/capita=','hours per person: ').replaceAll('wage_verdict=','Income test: ').replaceAll('payback_verdict=','payback test: ').replaceAll('take_home=','take-home: $').replaceAll('payback=','payback: ').replaceAll(' vs median=',' against median wage $').replaceAll('annual_gross_margin <= 0; payback never recoverable','Annual margin is nonpositive; capital cannot be recovered').replaceAll('market_price_per_unit absent or zero; entry not designed for market lens','No market selling price is available for this design')||'Both market tests meet the model’s favorable thresholds.';section.append(title,metric,explanation,notes);$('#lenses').append(section);}$('#population').textContent=`${result.population.toLocaleString('en-US')} people · ${result.households.toLocaleString('en-US')} households · draft catalog sensitivity`;
}
function submit(){
 if(!worker||!ready||active)return;
 clearTimeout(debounce);invalidate();
 const w=worker,gen=generation;
 active={id:++sequence,generation:gen,inputs:Object.freeze(inputs())};
 const request=active;
 busy(true);$('#status').textContent='Evaluating…';
 computeTimer=setTimeout(()=>{
  if(w===worker&&gen===generation&&active===request)
   fail('Evaluation exceeded the 15-second deadline. Worker stopped. Retry or read the catalog.');
 },DEADLINE_MS);
 try{
  w.postMessage({type:'evaluate',generation:gen,id:request.id,entry:Number(request.inputs.entry),
   scale:request.inputs.scale,participation:Number(request.inputs.participation)/100,wage:Number(request.inputs.wage)});
 }catch{fail('Evaluator could not accept the request. Retry or read the catalog.');}
}
function start(){
 stop();invalidate();labels();$('#status').textContent='Loading Rust evaluator…';
 const gen=++generation;let w;
 try{w=new Worker('./worker.js',{type:'module'});worker=w;}
 catch{fail('Evaluator could not load. Retry or read the catalog.');return;}
 busy(true);
 bootTimer=setTimeout(()=>{
  if(w===worker&&gen===generation)fail('Evaluator could not load within the 15-second deadline. Retry or read the catalog.');
 },DEADLINE_MS);
 w.onerror=event=>{
  event.preventDefault?.();
  if(w===worker&&gen===generation)fail('Evaluator could not load or continue. Retry or read the catalog.');
 };
 w.addEventListener('messageerror',()=>{
  if(w===worker&&gen===generation)fail('Evaluator returned an unreadable message. Retry or read the catalog.');
 });
 w.onmessage=({data})=>{
  if(w!==worker||gen!==generation||!data||typeof data!=='object'||data.generation!==gen)return;
  if(data.type==='ready'){
   if(ready)return;
   clearTimeout(bootTimer);ready=true;submit();return;
  }
  if(data.type==='error'&&!ready){fail('Evaluator could not load. Retry or read the catalog.');return;}
  if(!active||data.id!==active.id)return;
  if(data.type==='error'){fail(String(data.message));return;}
  if(data.type!=='result')return;
  clearTimeout(computeTimer);
  if(!validResult(data.result)||!Number.isFinite(data.ms)||data.ms<0){
   fail('Evaluator returned an invalid result. Retry or read the catalog.');return;
  }
  completed={inputs:active.inputs,result:structuredClone(data.result)};active=null;
  display(completed.result);busy(false);
  $('#status').textContent=`Evaluated in ${data.ms.toFixed(1)} ms · processing stays on your device`;
  $('#export').disabled=false;
 };
 try{w.postMessage({type:'init',generation:gen});}
 catch{fail('Evaluator could not load. Retry or read the catalog.');}
}
function edit(restart=false){
 const version=++sequence;clearTimeout(debounce);invalidate();labels();
 if(active){start();return;}
 if(!worker){
  if(restart)start();else $('#status').textContent='Assumptions updated. Retry evaluator when ready.';
  return;
 }
 if(!ready)return;
 busy(true);$('#status').textContent='Updating assumptions…';
 debounce=setTimeout(()=>{if(sequence===version)submit();},80);
}
for(const id of ['participation','wage'])$(`#${id}`).oninput=()=>edit();
for(const id of ['entry','scale'])$(`#${id}`).onchange=()=>edit();
$('#cancel').onclick=()=>fail('Evaluation cancelled. Assumptions are kept. Retry when ready.');
$('#retry').onclick=start;
$('#reset').onclick=()=>{
 $('#entry').value='0';$('#scale').value='town';$('#participation').value='2.5';$('#wage').value='56000';
 history.replaceState(null,'',location.pathname);$('#share-status').textContent='';edit(true);
};
$('#share').onclick=async()=>{
 const url=new URL(location.href);url.search='';
 for(const[id,value]of Object.entries(inputs()))url.searchParams.set(id,value);
 history.replaceState(null,'',url);
 try{await navigator.clipboard.writeText(url.href);}catch{}
 $('#share-status').textContent='Scenario link is in the address bar. It shares assumptions only.';
};
$('#export').onclick=()=>{
 if(!completed)return;
 if(JSON.stringify(inputs())!==JSON.stringify(completed.inputs)){edit();return;}
 const bytes=JSON.stringify({inputs:completed.inputs,result:completed.result,source_commit:SOURCE_COMMIT},null,2);
 const url=URL.createObjectURL(new Blob([bytes],{type:'application/json'}));
 const link=document.createElement('a');link.href=url;link.download='ceres-draft-evaluation.json';link.click();
 setTimeout(()=>URL.revokeObjectURL(url),1000);
};
const params=new URLSearchParams(location.search);
for(const[id,min,max,step]of [['entry',0,1,1],['participation',0.1,20,0.1],['wage',10000,200000,1000]]){
 const n=Number(params.get(id));
 if(params.has(id)&&Number.isFinite(n)&&n>=min&&n<=max&&Math.abs(n/step-Math.round(n/step))<1e-8)$(`#${id}`).value=n;
}
if(['village','town','small_city'].includes(params.get('scale')))$('#scale').value=params.get('scale');
for(const id of [...fields,'reset','share'])$(`#${id}`).disabled=false;
start();
