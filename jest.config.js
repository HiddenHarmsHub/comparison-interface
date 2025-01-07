/* global module */
module.exports = {

    "roots": [
        'tests_accessibility/',
        'tests_javascript/'
    ],

    "setupFiles": [
        "<rootDir>/jest_setup_files/jquery_setup.js"
    ],

    "setupFilesAfterEnv": [
        "<rootDir>/jest_setup_files/accessibility_testing_setup.js"
    ]

}
