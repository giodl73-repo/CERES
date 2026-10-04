import {test,expect} from '@playwright/test';
test('actual Rust lenses respond to participation and share/export',async({page})=>{
 const errors=[];page.on('pageerror',e=>errors.push(e.message));const wasm=page.waitForResponse(r=>r.url().endsWith('.wasm'));await page.goto('/CERES/?entry=1&scale=village&participation=0.1');expect((await wasm).status()).toBe(200);await expect(page.locator('#coop .badge')).toHaveText('fail');
 await page.locator('#participation').evaluate(e=>{e.value='20';e.dispatchEvent(new Event('input'));});await expect(page.locator('#coop .badge')).not.toHaveText('fail');
 await page.locator('#share').click();await page.reload();await expect(page.locator('#participation')).toHaveValue('20');await expect(page.locator('#coop .badge')).not.toHaveText('fail');
 const download=page.waitForEvent('download');await page.locator('#export').click();expect((await download).suggestedFilename()).toBe('ceres-draft-evaluation.json');expect(errors).toEqual([]);
});
test('mobile invalid query and WASM failure stay readable',async({page})=>{
 await page.setViewportSize({width:390,height:844});await page.goto('/CERES/?entry=9&wage=NaN');await expect(page.locator('#lenses .lens')).toHaveCount(3);expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBeTruthy();
 await page.route('**/*.wasm',r=>r.fulfill({status:503,body:'unavailable'}));await page.reload();await expect(page.locator('#status')).toContainText('could not load');await expect(page.locator('#export')).toBeDisabled();
});
