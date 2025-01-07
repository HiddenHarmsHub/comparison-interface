/* global require */
const fs = require('fs');
const path = require('path');

const reportFolder = "accessibility_reports";

if (!fs.existsSync(reportFolder)) {
    fs.mkdirSync(reportFolder);
} else {
    fs.readdirSync(reportFolder).forEach(file => fs.rmSync(path.join(reportFolder, file), {recursive:true}));
}
