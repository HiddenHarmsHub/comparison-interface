---
id: installation
title: Installation
---

The software can be run on any operating system and requires Python 3.9 or higher.

If you are working in an IDE which supports dev containers then the quickest way to get started with the software is to use the dev container configuration provided in the repository to create a dev container in your IDE. The dev container configuration contains all of the dependencies required to run the software as well as all of the test suites and the linters used in the CI.

If you are not using the dev container you will need to install the dependencies in the requirements.txt file. Using a python virtual environment is recommended but it is not necessary. If you want to run the Python linters and tests you will also need the dependencies in the requirements-test.txt file. The JavaScript and accessibility test requirements are covered in the [testing section](testing.md).

To set up the virtual environment and install the python requirements use the following commands.

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

If you are using windows then you may need to change the way the that you activate the virtual environment (the second line in the example above) and instead use one of the following two lines of code depending on the type of shell you are using.

For CMD:

```ps
.\venv\Scripts\activate.bat
```

For Power shell:

```ps
.\venv\Scripts\activate.ps1
```

Flask provides a development webserver which is good enough to evaluate the software and for local testing/development. For use in production follow the advice provided in the [Flask documentation](https://flask.palletsprojects.com/en/3.0.x/deploying/).

## Running the provided examples

This sequence of commands will allow you setup and run one of the pre-configured examples. Examples are provided for each of the three types of item pair selection described in the introduction, the example files can be found in the `examples` directory inside the `comparison_interface` directory.

1. equal item weight options
    + config-equal-item-weights.json
    + config-equal-item-weights-preference.json
1. config-custom-item-weights.json

### Initial setup

If you are not using the dev container provided then:

+ rename the `example.images` file in `comparison_interface/static/` to `images`.
+ rename the `example.flask.py` file in `comparison_interface/configuration/` to `flask.py`.

When running in production the secret key in the flask.py should also be changed.

Open a terminal and run these commands replacing ```[configuration_file_name]``` with the name of the configuration file you want to try.

```bash
flask --debug setup examples/[configuration_file_name]
flask --debug run --port=5001
```

In your browser navigate to <http://localhost:5001>

You should see the registration page of the website and all of the functions should be working so you can test the features with a small set of images.

Any free port number can be used to host the website by changing the port number in the run command. 5001 is used in all of the examples because it is the port number that is open in the dev container setup mentioned above.

### Resetting the system

Once the setup command used above has been run and a database has been created it cannot be used again unless the database file is manually deleted.

To reset the database and switch to a different configuration the reset command should be used. This is a destructive process as it will delete the current database along with any data in it and also delete any exported files still in the export location. Before the first of these commands actually does anything you will be given a warning that the operation will delete these files and you will need to confirm that you want to go ahead with the database reset.

```bash
flask --debug reset examples/[configuration_file_name]
flask --debug run --port=5001
```
