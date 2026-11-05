import init,{evaluate_json} from './pkg/ceres_web.js';
self.onmessage=async({data})=>{try{if(data.type==='init'){await init();self.postMessage({type:'ready'});}else{
// Guard before wasm32 usize conversion: raw JS fractions/large integers can alias 0 or 1.
if(!Number.isSafeInteger(data.entry)||data.entry<0||data.entry>1)throw new Error('Choose a draft entry index 0 or 1; integer conversion rejected.');
const started=performance.now(),result=JSON.parse(evaluate_json(data.entry,data.scale,data.participation,data.wage));self.postMessage({type:'result',id:data.id,result,ms:performance.now()-started});}}catch(e){self.postMessage({type:'error',id:data?.id,message:String(e)});}};
