import {test,expect} from '@playwright/test';
import {createHash} from 'node:crypto';
import {spawnSync} from 'node:child_process';
import fs from 'node:fs';

for(const [name,viewport] of [['desktop',{width:1280,height:900}],['mobile',{width:390,height:844}]]){
 test(`${name}: complete source download is optional and survives failed WASM`,async({page,request},info)=>{
  await page.setViewportSize(viewport);
  const sourceRequests=[],downloads=[];
  page.on('request',r=>{if(r.url().endsWith('/ceres-source.zip'))sourceRequests.push(r.url());});
  page.on('download',d=>downloads.push(d.suggestedFilename()));
  await page.route('**/*.wasm',r=>r.fulfill({status:503,body:'unavailable'}));
  await page.goto('/CERES/');await expect(page.locator('#status')).toContainText('could not load');
  expect(sourceRequests).toEqual([]);expect(downloads).toEqual([]);
  const response=await request.get('/CERES/BUILD-MANIFEST.json');expect(response.ok()).toBeTruthy();
  const build=await response.json();expect(build.source_commit).toMatch(/^[a-f0-9]{40}$/);
  await expect(page.locator('#source-revision')).toHaveText(build.source_commit);
  await expect(page.locator('#catalog-link')).toHaveAttribute('href',new RegExp(`/blob/${build.source_commit}/catalog/`));
  expect(build.sizes.runtime).toBeLessThan(5_000_000);expect(build.sizes.downloads).toBeLessThan(12_000_000);
  await page.locator('#source-download').scrollIntoViewIfNeeded();await page.locator('#source-download').focus();
  const pending=page.waitForEvent('download');await page.keyboard.press('Enter');const download=await pending;
  const target=info.outputPath('ceres-source.zip');await download.saveAs(target);
  expect(createHash('sha256').update(fs.readFileSync(target)).digest('hex')).toBe(build.source.sha256);
  const verified=spawnSync('python',['tools/receive-source.py','--source',target,'--sha256',build.source.sha256,'--commit',build.source_commit],{encoding:'utf8',timeout:30000});
  expect(verified.status,verified.stderr).toBe(0);expect(JSON.parse(verified.stdout).git_blobs).toBeGreaterThanOrEqual(300);
  expect(downloads).toEqual(['ceres-source.zip']);
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBeTruthy();
  await page.screenshot({path:info.outputPath('source-route.png'),fullPage:true});
 });
}
