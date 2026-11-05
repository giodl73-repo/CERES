import init,{evaluate_json} from './pkg/ceres_web.js';
let engine;
self.onmessage=async({data})=>{
 try{
  if(!data||typeof data!=='object'||Array.isArray(data))throw new Error('Invalid evaluator request.');
  if(data.type==='init'){
   await(engine??=init());self.postMessage({type:'ready',generation:data.generation});return;
  }
  if(data.type!==undefined&&data.type!=='evaluate')throw new Error('Unknown evaluator request.');
  // Guard before wasm32 usize conversion; keep original Rust float/scale admission.
  if(!Number.isSafeInteger(data.entry)||data.entry<0||data.entry>1)
   throw new Error('Choose a draft entry index 0 or 1; integer conversion rejected.');
  await(engine??=init());
  const started=performance.now();
  const result=JSON.parse(evaluate_json(data.entry,data.scale,data.participation,data.wage));
  self.postMessage({type:'result',generation:data.generation,id:data.id,result,ms:performance.now()-started});
 }catch(error){
  self.postMessage({type:'error',generation:data?.generation,id:data?.id,message:String(error)});
 }
};
