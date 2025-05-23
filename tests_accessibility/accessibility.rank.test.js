/* global require, beforeAll, afterAll, describe, test, expect */

const pa11y = require('pa11y');
const puppeteer = require('puppeteer');

let browser;

beforeAll(async () => {
    browser = await puppeteer.launch({
      headless: "new",
      args: ['--no-sandbox']
    });
  });
  
  afterAll(async () => {
    await browser.close();
  });

  describe('Test the rank page', () => {

    test('Test the rank page', async () => {
        const page = await browser.newPage();
        page.setDefaultTimeout(100000);
        const url = 'http://localhost:5001/rank';
        //let itemId, currentId;
        await page.goto(url, {waitUntil: 'networkidle0'});
        // accept the cookies
        await page.waitForSelector('#cookie-message-popup-accept', { visible: true });
        page.click('#cookie-message-popup-accept');
        // fill in the form (using the type function did not work for me)
        await page.waitForSelector('#cookie-message-popup-accept', { visible: false });
        await page.$eval('#name-input', el => el.value = 'My Name');
        page.click('#country-choice-1');
        await page.select('#allergies-select', 'Yes');
        await page.$eval('#age-input', el => el.value = '29');
        await page.$eval('#email-input', el => el.value = 'test@example.com');
        await page.$eval('#group-2', el => el.checked = 'true');
        await page.$eval('#accept-ethics-agreement', el => el.checked = 'true');
        expect(await page.$eval('#group-2', el => el.checked)).toBe(true);
        expect(await page.$eval('#accept-ethics-agreement', el => el.checked)).toBe(true);
        // submit the form
        page.click('#submit-button');

        // work through the items for selection
        // await page.waitForSelector('#agree-button', { visible: true });
        // itemId = await page.$('#item-id');
        // currentId = await page.evaluate(el => el.value, itemId)
        // page.click('#agree-button');

        // await page.waitForNavigation({ waitUntil: 'networkidle0' });
        // expect(await page.$eval('#item-id', el => el.value)).not.toBe(currentId);
        // itemId = await page.$('#item-id');
        // currentId = await page.evaluate(el => el.value, itemId)
        // page.click('#agree-button');

        // await page.waitForNavigation({ waitUntil: 'networkidle0' });
        // expect(await page.$eval('#item-id', el => el.value)).not.toBe(currentId);
        // itemId = await page.$('#item-id');
        // currentId = await page.evaluate(el => el.value, itemId)
        // page.click('#agree-button');

        // wait for the ranking page to load
        await page.waitForNavigation({ waitUntil: 'networkidle0' });
        await page.waitForSelector('#confirm-button-d', { visible: true });

        // run pa11y and test the report
        const report = await pa11y(url, {
            runners: ['axe', 'htmlcs'],
            standard: 'WCAG2AA',
            ignoreUrl: true,
            browser: browser,
            page: page,
            includeWarnings: false,
            includeNotices: false
        });
        await expect(report).toHaveNoErrors();
    }, 100000);

});