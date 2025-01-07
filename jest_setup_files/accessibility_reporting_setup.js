/* global require, expect */
const fs = require('fs');
const path = require('path');
const pa11y = require('pa11y');
const htmlReporter = require('pa11y/lib/reporters/html');

const pa11y_options = {
    "chromeLaunchConfig": {"args": ["--no-sandbox"]},
    "runners": ["axe", "htmlcs"],
    "includeWarnings": true,
    "includeNotices": true
};

const reportFolder = "accessibility_reports";

function writeReport(report, url) {
    let filename = url.split('/').pop();
    let outputPath = path.join(reportFolder, filename + '.html');
    let i = 1;
    while (fs.existsSync(outputPath)) {
        let new_filename = filename + '_' + i;
        outputPath = path.join(reportFolder, new_filename + '.html');
        i += 1;
    }
    fs.writeFileSync(outputPath, report);
}

expect.extend({
    async toBeAccessible (url, actions, waitTime) {
        const options = pa11y_options;
        if (actions !== undefined) {
            options["actions"] = actions;
        }
        if (waitTime !== undefined) {
            options["wait"] = waitTime;
        }
        const report = await pa11y(url, options);
        const htmlReport = await htmlReporter.results(report);
        writeReport(htmlReport, url);
        return {
            pass: true
        }
    }
});

expect.extend({
    async allToBeAccessible(urls) {
        let report, htmlReport;
        for (let i = 0; i < urls.length; i += 1) {
            report = await pa11y(urls[i], pa11y_options);
            htmlReport = await htmlReporter.results(report);
            writeReport(htmlReport, urls[i]);
        }
        return {
            pass: true
        }
    
    }
});

expect.extend({
    async toHaveNoErrors(report, filename) {
        const htmlReport = await htmlReporter.results(report);
        writeReport(htmlReport, filename);
        return {
            pass: true
        }
    }
});