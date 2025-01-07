/* global module */
module.exports = {

    "roots": [
        'tests_accessibility/'
    ],

    "setupFiles": [
        "<rootDir>/jest_setup_files/jquery_setup.js",
        "<rootDir>/jest_setup_files/prepare_reporting_directory.js"
    ],

    "setupFilesAfterEnv": [
        "<rootDir>/jest_setup_files/accessibility_reporting_setup.js"
    ]

}