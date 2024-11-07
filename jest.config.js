/* global module */
module.exports = {

    "roots": [
        'tests_accessibility/',
        'tests_javascript/'
    ],

    "setupFiles": [
        "./jquery_setup.js"
    ],

    "setupFilesAfterEnv": [
        "./accessibility_testing_setup.js"
    ]

}
