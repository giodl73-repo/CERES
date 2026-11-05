import {test,expect} from '@playwright/test';
import fs from 'node:fs/promises';
import crypto from 'node:crypto';
const manifest=JSON.parse(await fs.readFile(new URL('../../notices/manifest.json',import.meta.url),'utf8'));
const sha=bytes=>crypto.createHash('sha256').update(bytes).digest('hex');
test('actual pinned Cargo/runtime notices download independently of a failed engine',async({page})=>{
 await page.route('**/*.wasm',route=>route.fulfill({status:503,body:'unavailable'}));
 await page.goto('/CERES/');await expect(page.locator('#status')).toContainText('could not load');
 for(const [name,expected]of [['Cargo dependency notices',manifest.notices_sha256],['Rust runtime notices',manifest.rust_runtime.sha256]]){
  const pending=page.waitForEvent('download');await page.getByRole('link',{name,exact:true}).click();const download=await pending;
  expect(sha(await fs.readFile(await download.path()))).toBe(expected);
 }
 await expect(page.getByRole('link',{name:'Complete source ZIP · includes build inputs',exact:true})).toHaveAttribute('href','downloads/ceres-source.zip');
});
