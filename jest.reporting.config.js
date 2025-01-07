/* global module */
module.exports = {

    "roots": [
        'tests_accessibility/'
    ],

    "setupFiles": [
        "./jquery_setup.js"
    ],

    "setupFilesAfterEnv": [
        "./accessibility_reporting_setup.js"
    ]

}