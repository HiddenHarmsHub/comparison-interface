---
id: testing
title: Running the Tests
---

Three different kinds of tests are provided, Python tests, JavaScript tests and accessibility tests.

All of the dependencies needed to run the full suite of tests are included in the dev container.

If you are not using the dev container, to run the Python tests you will need to install the dependencies in the `test` section of the pyproject.toml.

To run the JavaScript and accessibility tests you need to install Node and then the dependencies in the `package.json` file provided. In addition you need to install a Chrome browser for Puppeteer (this is used for the accessibility tests). The dependencies can be installed as follows (run from the root of the repository):

```bash
npm install
npx puppeteer browsers install chrome
```

## Python tests

The Python tests are written in pytest and can be found in the tests_python folder. The tests are run as follows:

```bash
pytest
```

**Note:** The configuration files used for testing are not the same as the example configuration files provided with the software. The configuration files used by the tests can be found in the `test_configurations` folder inside the `tests_python` folder.

## JavaScript tests

The JavaScript tests are written in Jest. They are run as follows:

```bash
npx jest -- tests_javascript
```

## Accessibility tests

The accessibility tests are written in Jest and use Pa11y. Because of the multiple configuration options available the tests are split and need to be run against two different configurations on the flask app.

The Flask application must be setup with the correct configuration file from the `tests_python/test_configurations` and be running at `http://localhost:5001` for these tests to run successfully. Most of the tests run with the `/tests_python/test_configurations/config-equal-item-weights-2.json` configuration file.

To setup the system for the main test file (the setup may need to be replaced with the `reset` command if you already have a database in use):

```bash
flask --debug setup ../tests_python/test_configurations/config-equal-item-weights-2.json
flask --debug run ---port=5001
```

The tests can then be run as follows:

```bash
npx jest -- tests_accessibility/accessibility.test.js
```

To run the additional test file:

```bash
flask --debug reset ../tests_python/test_configurations/config-equal-item-weights.json
flask --debug run ---port=5001
```

The tests can then be run as follows:

```bash
npx jest -- tests_accessibility/accessibility-item-select.test.js
```

The first set of tests will probably be enough for most changes to the system. The second test only tests the item select page used when the `renderUserItemPreferencePage` key in the configuration file is set to `true`.

It is important to remember that automated accessibility tests cannot alone determine whether a website is fully accessible. Manual tests are also required; several browser plugins are available to help with this, one of the most comprehensive is [Accessibility insights for web](https://accessibilityinsights.io/docs/web/overview/).
