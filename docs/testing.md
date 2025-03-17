---
id: testing
title: Running the Tests
---

Three different kinds of tests are provided, Python tests, JavaScript tests and accessibility tests.

To run the python tests you will need to install the dependencies in the requirements-test.txt.

To run the JavaScript and accessibility tests you need to install Node and then the dependencies in the package.json file provided. In addition you need to install a chrome browser for puppeteer (this is used for the accessibility tests). The depencies can be installed as follows:

```bash
npm install
npx puppeteer browsers install chrome
```

All of the dependencies needed to run the full suite of tests are included in the dev container.

## Python tests

The Python tests are written in pytest and can be found in the tests_python folder. The tests are run as follows:

```bash
pytest
```

**Note:** The configuration files used for testing are not the same as the example configuration files provided with the software. The configuration files used by the tests can be found in the ```test_configurations``` folder inside the ```tests_python``` folder.

## JavaScript tests

The JavaScript tests are written in Jest. They are run as follows:

```bash
npx jest -- tests_javascript
```

## Accessibility tests

The accessibility tests are written in Jest and use Pa11y. The flask application must be running at ```http://localhost:5001``` for these tests to run successfully. They are run as follows:

```bash
npx jest -- tests_accessibility
```