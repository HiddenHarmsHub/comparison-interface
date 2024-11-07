/* global require, expect */
const pa11y = require('pa11y');
const cliReporter = require('pa11y/lib/reporters/cli');

function checkReport(report) {
    const errors = report.issues;
    const failures = [];
    for (let i = 0; i < errors.length; i += 1) {
        if (errors[i].typeCode === 1) {
            failures.push(errors[i])
        }
    }
    return failures;
}

expect.extend({
    async toBeAccessible (url, actions, waitTime) {
        const options = {"chromeLaunchConfig": {"args": ["--no-sandbox"]},
                         "runners": ["axe", "htmlcs"]};
        if (actions !== undefined) {
            options["actions"] = actions;
        }
        if (waitTime !== undefined) {
            options["wait"] = waitTime;
        }
        const report = await pa11y(url, options);
        const result = checkReport(report);
        if (result.length > 0) {
            const results = await cliReporter.results(report)
            return {
                pass: false,
                message: () => results
            }
        } else {
            return {
                pass: true
            }
        }
    }
});

expect.extend({
    async allToBeAccessible(urls) {
        let report;
        let fail = false;
        let results = '';
        const options = {"chromeLaunchConfig": {"args": ["--no-sandbox"]},
                         "runners": ["axe", "htmlcs"]};
        for (let i = 0; i < urls.length; i += 1) {
            report = await pa11y(urls[i], options);
            const result = checkReport(report);
            if (result.length > 0) {
                fail = true;
                results = results.concat(await cliReporter.results(report));
            } 
        }
        if (fail) {
            return {
                pass: false,
                message: () => results
            }
        } else {
            return {
                pass: true
            }
        }
    }
});

expect.extend({
    async toHaveNoErrors(report) {
        const result = checkReport(report);
        if (result.length === 0) {
            return {
                pass: true
            }
        } else {
            const results = await cliReporter.results(report)
            return {
                pass: false,
                message: () => results
            }
        }
    }
});
