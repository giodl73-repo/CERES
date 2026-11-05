import {test,expect} from '@playwright/test';
import fs from 'node:fs';
const original=JSON.parse(fs.readFileSync(new URL('../fixtures/reader-original.json',import.meta.url),'utf8'));

test('real worker retains all120 original successful native results',async({page})=>{
 await page.goto('/CERES/');
 const actual=await page.evaluate(async cases=>{
  const worker=new Worker('/CERES/worker.js',{type:'module'});
  const receive=()=>new Promise((resolve,reject)=>{const timer=setTimeout(()=>reject(Error('Worker observation timeout')),15000);worker.onmessage=({data})=>{clearTimeout(timer);resolve(data);};worker.onerror=()=>{clearTimeout(timer);reject(Error('Worker observation failed'));};});
  try{
   let next=receive();worker.postMessage({type:'init'});if((await next).type!=='ready')throw Error('Worker not ready');
   const rows=[];
   for(let i=0;i<cases.length;i++){
    const {args}=cases[i];next=receive();worker.postMessage({id:i+1,entry:Number(args[0]),scale:args[1],participation:Number(args[2]),wage:Number(args[3])});
    const data=await next;if(data.type!=='result'||data.id!==i+1)throw Error('Unexpected worker result');rows.push(data.result);
   }
   return rows;
  }finally{worker.terminate();}
 },original.cases);
 expect(actual).toEqual(original.cases.map(row=>row.result));
});

test('worker rejects fractional, out-of-width and nonnumber entries before ABI aliasing',async({page})=>{
 await page.goto('/CERES/');
 const result=await page.evaluate(async()=>{
  const worker=new Worker('/CERES/worker.js',{type:'module'});
  const receive=()=>new Promise((resolve,reject)=>{const timer=setTimeout(()=>reject(Error('Worker observation timeout')),15000);worker.onmessage=({data})=>{clearTimeout(timer);resolve(data);};});
  try{
   let next=receive();worker.postMessage({type:'init'});if((await next).type!=='ready')throw Error('Worker not ready');
   const values=[4294967296,4294967297,1.5,Number('18446744073709551615'),-1,2,0.5,NaN,Infinity,-Infinity,null,undefined,'0',[],{}];const rows=[];
   for(let i=0;i<values.length;i++){next=receive();worker.postMessage({id:i+1,entry:values[i],scale:'town',participation:0.025,wage:56000});rows.push(await next);}
   next=receive();worker.postMessage({id:100,entry:1,scale:'town',participation:0.025,wage:56000});const valid=await next;
   return {rows,valid};
  }finally{worker.terminate();}
 });
 expect(result.rows).toHaveLength(15);
 result.rows.forEach((row,i)=>{expect(row.type).toBe('error');expect(row.id).toBe(i+1);expect(row.message).toContain('integer conversion rejected');});
 expect(result.valid.type).toBe('result');expect(result.valid.id).toBe(100);expect(result.valid.result.status).toBe('draft catalog sensitivity; not validated');
});
