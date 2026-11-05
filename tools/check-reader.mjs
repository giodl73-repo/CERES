// Observe the original typed Rust reader on native and actual unknown-target WASM.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {spawnSync} from 'node:child_process';
import crypto from 'node:crypto';

const [glue,native,output]=process.argv.slice(2);
if(!output)throw Error('Usage: node tools/check-reader.mjs <web-glue.js> <native-reader-control> <new-result.json>');
if(fs.existsSync(output))throw Error('Use a new observation output');
const modulePath=path.join(path.dirname(glue),'ceres_web_bg.wasm');
const bytes=fs.readFileSync(modulePath),compiled=await WebAssembly.compile(bytes);
const imports=WebAssembly.Module.imports(compiled);
const {default:init,evaluate_json}=await import(pathToFileURL(path.resolve(glue)));
await init({module_or_path:bytes});
const cases=[];
for(const entry of ['0','1'])for(const scale of ['village','town','small_city'])
for(const participation of ['0.001','0.025','0.1','0.2'])for(const wage of ['10000','48000','56000','62000','200000'])
 cases.push([entry,scale,participation,wage]);
cases.push(['2','town','0.025','56000'],['4294967295','town','0.025','56000'],['0','planet','0.025','56000']);
for(const value of ['0','0.0009','0.20001','NaN','inf','-inf'])cases.push(['0','town',value,'56000']);
for(const value of ['0','9999','200001','NaN','inf','-inf'])cases.push(['0','town','0.025',value]);
function number(value){return value==='inf'?Infinity:value==='-inf'?-Infinity:Number(value);}
function observe(args){
 const p=spawnSync(native,args,{encoding:'utf8',timeout:15000});
 if(p.error)throw p.error;
 const control=p.status===0&&!p.stderr?JSON.parse(p.stdout):{transport_error:true,exit:p.status,stdout:p.stdout,stderr:p.stderr};
 let wasm;try{wasm={ok:true,json:evaluate_json(number(args[0]),args[1],number(args[2]),number(args[3]))};}
 catch(error){wasm={ok:false,error:String(error)};}
 const exact=control.ok===wasm.ok&&(control.ok?control.json===wasm.json:control.error===wasm.error);
 return {args,native:control,wasm,exact};
}
const rows=cases.map(observe);
// These raw JS integer inputs are outside the reader's entry=0|1 UI domain.
// Bindgen's usize ABI coercion is recorded separately, never hidden as parity.
const seams=['4294967296','4294967297','1.5','18446744073709551615'].map(entry=>observe([entry,'town','0.025','56000']));
const result={schema:'ceres.original-reader-parity.v1',controls:rows.length,all_exact:rows.every(row=>row.exact),rows,
  imports,raw_js_integer_abi_seams:seams,abi_seams_are_ui_admitted:false,
  wasm_sha256:crypto.createHash('sha256').update(bytes).digest('hex'),wasm_bytes:bytes.length,
  scope:'Original typed reader parity and separately observed raw JS integer conversion, not economic/catalog/source/delivery validation'};
fs.writeFileSync(output,JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({controls:rows.length,all_exact:result.all_exact,imports,raw_js_abi_differences:seams.filter(row=>!row.exact).length,wasm_sha256:result.wasm_sha256,wasm_bytes:bytes.length}));
if(!result.all_exact)process.exitCode=1;
