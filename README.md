# Comparison Interface V2

This repository provides a web interface to facilitate the collection of comparative judgement data. It offers a highly configurable interface which only requires a configuration file and a set of image files as input. Data is stored in an SQLite database which is part of the standard python library so no additional database is required. There is no restriction regarding the nature of the items that can be compared in the software but it has been used previously on geospatial datasets to be processed with the [Bayesian Spatial Bradley--Terry model BSBT](https://github.com/rowlandseymour/BSBT).

The images presented to the user are selected in different ways depending on the configuration of the system.

1. Equally weighted pairs
    * A random pair of images from one of the selected groups or the full image set if only one group is defined.
    * A random pair of images from those items the user has knowledge of (these are selected in a pre-judging step also provided in the interface).
1. A pair of images selected in line with the weights assigned to the pair in the config file (the higher the weight the more likely the pair is to be presented).

Example configuration files for each of these models are provided with the application along with a small set of images.

This version of software expands over the initial application build by Bertrand Perrat that can be found [here](https://github.com/BPerrat/BSBT-Interface). The code in this version of the interface was written by Fabián Hernández with additional features and general updates by Catherine Smith in the Research Software Group, part of Advanced Research Computing, University of Birmingham.

## Terms

* **judge**: Person who makes the comparison between items.
* **groups**: The item's natural clustering.

## Main features.

1. The entire text of the website can be changed in configuration files.
1. Custom weights can be defined for pairs of items.
1. Multiple item groups can be defined to allow item selection at a higher level.
1. The user registration page is configurable to collect the user data required for the study.
1. The entire database can be dumped to a zip file containing either csv or tsv files.
1. A limit can be set for the number of judgements that can be made by a single user. (optional)
1. Instructions can be written/formatted in Google docs and then rendered on the website keeping the original look and feel. (optional)
1. Ethics agreement can be written/formatted in Google docs and then rendered on the website keeping the original look and feel. (optional)
1. Ethics agreement acceptance can be configured to be mandatory at registration. (This is an optional feature)
1. Site Policies can be written/formatted in Google docs and then rendered on the website keeping the original look and feel. (optional).
1. Cookies footer can be render and asked to be accepted by the judge. (optional).
1. The Website interface will render adequately on mobile devices as well as on larger screens.
1. The website meets WCAG 2.2 AA accessibility guidelines.

## Running the Software

The software can be run on any operating system and requires python 3.9 or higher.

If you are working in an IDE which supports dev containers then the quickest way to get started with the software is to use the dev container configuration provided in the repository to create a dev container in your IDE. The dev container configuration contains all of the dependencies required to run the software as well as all of the test suites and the linters used in the CI.

If you are not using the dev container you will need to install the dependencies in the requirements.txt file. Using a python virtual environment is recommended but it is not necessary. If you want to run the python linters and tests you will also need the dependencies in the requirements-test.txt file. The JavaScript and accessibility test requirements are covered in the testing section below.

To set up the virtual environment and install the python requirements ensure VirtualEnv is is available and use the following commands.

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install requirements.txt
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

### Running the provided examples

This sequence of commands will allow you setup and run one of the pre-configured examples. Examples are provided for each of the three types of item pair selection described in the introduction.

1. equal item weight options
    * config-equal-item-weights.json
    * config-equal-item-weights-preference.json
1. config-custom-item-weights.json

#### Initial setup

Open a terminal and run these commands replacing ```[configuration_file_name]``` with the name of the configuration file you want to try.

```bash
flask --debug setup examples/[configuration_file_name]
flask --debug run --port=5001
```

In your browser navigate to <http://127.0.0.1:5001>

You should see the registration page of the website and all of the functions should be working so you can test all of the features with a small set of images.

Any free port number can be used to host the website by changing the port number in the run command. 5001 is used in all of the examples because it is the port number that is open in the dev container setup mentioned above.

#### Resetting the system

Once the setup command used above has been run and a databsae has been created it cannot be used again unless the database file is manually deleted.

To reset the database and switch to a different configuration for testing the reset command should be used. This is a destructive process as it will delete the current database along with any data in it and also delete any exported files still in the export location.

```bash
flask --debug reset examples/[configuration_file_name]
flask --debug run --port=5001
```

### Customising the system

Please follow the next step to make a custom configuration for a project.

#### Requirements

1. The images of the items being compared.
    * These images must be at least 300x300 pixels.
    * The file names of the images must be unique.
    * Valid image formats: png, jpg or jpeg.
1. Configure the language settings if not using English (see below for more guidance).
1. Create your configuration file (see below for more guidance).
1. (optional) Create and [publish](https://support.google.com/docs/answer/183965?hl=en&co=GENIE.Platform%3DDesktop) your own ethics agreement Google Document.
1. (optional) Create and [publish](https://support.google.com/docs/answer/183965?hl=en&co=GENIE.Platform%3DDesktop) your own introduction Google Document.
1. (optional) Create and [publish](https://support.google.com/docs/answer/183965?hl=en&co=GENIE.Platform%3DDesktop) your own site policies Google Document.

#### Steps

1. Replace the contents of the folder ***static/images*** with your own images.
1. Copy your configuration file to the folder ***examples/*** or another location within the comparison_interface directory.
1. Open a terminal and run these commands.

    ```bash
    flask --debug setup [path_to_configuration_file]
    flask --debug run --port=5001
    ```

1. Navigate in you preferred browser to <http://127.0.0.1:5001>

## Language configuration

All the the text that a user sees on the website can be configured. Any strings which are language rather than project specific are stored in the language file in the languages directory. The sample file is ```en.json``` and contains all of the non project specific strings in English. This file is a JSON file and can be copied and edited to be used for other languages. All of the keys in the JSON should be present for any additional languages generated and the iso code for the language used to name the file for example ```en.json``` or ```de.json```. Any string can actually be used for the file name as long as that same string is used in the language setting described below but using the iso code will help others understand the system.

To tell the system which file to use change the setting in the ```flask.py``` file in the ```configuration``` directory. The configuration for English is as follows:

```python
    LANGUAGE = 'en'
```

This will look for the display strings in ```languages/en.json```.

If the language strings do need to be changed for a specfic project, then any of the keys in the language file can be included in the project configuration file described below and these will be displayed instead of the strings set in the language file.

## Creating your configuration file

The configuration file is written in JSON and has four sections.

1. **behaviourConfiguration** defines the settings to control the behaviour of the system including what links are present in the header
1. **userFieldsConfiguration** details the questions that the user is asked on the registration page
1. **websiteTextConfiguration** defines the text that the user sees on the website
1. **comparisonConfiguration** describes the images bsing used for the project and how they should be selected for comparison

When the system is started the configuration file requested will be validated and if there are any problems with the file the error message should help to fix them.

The easiest way to create a configuration file is to start with one of the three existing examples and modify that to meet the requirements of the project. Each of the sections will be covered below.

### Behaviour configuration

This section controls aspects of how the system works.

The ```exportPathLocation``` is required and determines where exported data files are saved when the database is exported.

Three required boolean values determine which links appear in the header of the webpage. If any of these booleans are set to true either the corresponding link key or the corresponding html key is required. If using the link key this should point to a [published google document](https://support.google.com/docs/answer/183965?hl=en&co=GENIE.Platform%3DDesktop). If using the html key then the HTML fragment should be wrapped in a ```<div>``` and contain the HTML you want to be displayed in the template. The template will take care of the header itself.

The keys and their corresponding link/html keys are listed below.

* renderUserInstructionPage
  * userInstructionLink
  * userInstructionHtml
* renderEthicsAgreementPage
  * userEthicsAgreementLink
  * userEthicsAgreementHtml
* renderSitePoliciesPage
  * sitePoliciesLink
  * sitePoliciesHtml

There is also a required boolean key ```renderCookiesFooter```, which determines whether the user is asked to accept the website cookies when first opening the website. The text for the cookie footer is stored in the language file but it you want to customise if for a particular project then the ```siteCookiesText``` key can be added to the project configuration with the string you want to display.

Three further boolean keys are required.

```renderUserItemPreferencePage``` determines whether the user is asked to specify whether they know each item in the set of items to be judged. For large item sets it is probably best to determine a users knowledge based on groups rather than individual items and set this value to false. However, it can be used in combination with the group preferences to add an extra level of selection if required. For weighted item configurations this boolean should be set to false.

```allowTies``` determines whether or not the system allows a user to select both images and record a tied result. Set this to true if you want to include ties in your study and to false if you do not.

```offerEscapeRouteBetweenCycles``` determines whether a user can continue making judgements indefinitely or if they are offered an opportunity to either logout or continue making judgements after reaching a target number. If this is set to true then two further keys are required. ```cycleLength``` specifies how many comparisons should be made in each cycle and ```maximumCyclesPerUser``` determines how many cycles each user is permitted to complete before no more comparisons will be presented to them.

### User fields configuration

This section configures all of the questions that the user is asked when registering on the system with the exception of the ethics agreement statement, this is configured in the behaviour section.

If no user registration questions are required then the userFieldsConfiguration can just be an empty list as follows:

```json
{
    "userFieldsConfiguration": []
}
```

If questions are required then the configuration for each question needs to be added to the list.

The supported html widget types are:

* text
* int
* radio
* dropdown
* email

An example of the full configuration for each of these types is provided in all of the example files. These can be used as a basis to construct your own questions.

### Website text configuration

There are up to four compusory keys (depending on the behaviour configuration) in the website configuration. There is one optional field. In addition, any of the fields in the language configuration file can be added into this section to override the language defaults should this be required.

All project configurations require the ```rankItemInstructionLabel``` key which is the text that is presented to the user along with the two images to make the judgement.

If the behaviour configuration ```renderUserItemPreferencePage``` is set to ```true``` then the ```itemSelectionQuestionLabel``` key is also required. This is the text presented to the user when they are selecting which items they know and will be followed by the image display name.

If multiple groups are defined in the comparison configuration section then the keys ```userRegistrationGroupQuestionLabel``` and ```userRegistrationGroupSelectionErr``` are required. The first is the text put alongside the group selection section of the registration page, the second is the error text displayed if no group has been selected and a user tries to register.

There is also an optional key for all projects ```additionalRegistrationPageText``` which instead of containing a string should contain a list of strings. These strings will be displayed on the registration page below any user questions and above the ethics approval statement (if used) and the registration button. This section can be used to display any required information to the user, the initial motivation for this section was to provide the relevant licensing information for all of the images used on the website.

### Comparison configuration

This section needs to define all of the images you want to use organised by groups and for weighted item pairs all of the weights.

Refer to **examples/config-equal-item-weights.json** or **examples/config-equal-item-weights-preference.json** to configure a scenario without any weighting for the item pairs and either with or without the item preference stage.

Refer to **examples/config-custom-item-weights.json** to configure a scenario where custom weights will be defined for all item pairs.

## Reset command

The reset command reloads the website configuration and resets the database. This command can be used when:

1. The website configuration file has been modified.
2. The content of the database needs to be deleted and reset.

**Note**: This is a destructive operation that will delete all the database content and any exported files in the original export location. You will be asked to confirm that you want to run the operation before the script will execute.

The command can be executed by typing:

```bash
flask --debug reset [path_to_configuration_file]
```

**Note**: If the configuration file is edited while the system is running then the system will have to be reset and all data in the database will be deleted. Once a system is running do not change a configuration file unless you want to reset the database.

## Exporting the data

The data in the database can be exported using the following command.

```bash
flask --debug export
```

This will export the database contents to a zip file containing one .csv file per database table, located at the location configured in the configuration json file. There is also an option to export the data to a zip file of .tsv files.

```bash
flask --debug export --format=tsv
```

There is also an option to expose the table containing the decisions made by users only (no user details) via a secured api. This is enabled by setting the 'API_ACCESS' variable in the ```configuration/flask.py``` file to ```True```. In addition a ```.apikey``` file needs to be created at the top level of the repository. This should contain the secret key which will be used to authenticate api calls. The file name used to store the key can be changed in the ```configuration/flask.py``` file.


## Testing

Three different kinds of tests are provided, Python tests, JavaScript tests and accessibility tests.

To run the python tests you will need to install dependencies in the requirements-test.txt.

To run the JavaScript and accessibility tests you need to install Node and then the dependencies in the package.json file provided. In addition you need to install a chrome browser for puppeteer (this is used for the accessibility tests). The depencies can be installed as follows:

```bash
npm install
npx puppeteer browsers install chrome
```

All of the dependencies needed to run the full suite of tests are included in the dev container.

### Python tests

The Python tests are written in pytest and can be found in the tests_python folder. The tests are run as follows:

```bash
pytest
```

**Note:** The configuration files used for testing are not the same as the example configuration files provided with the software. The configuration files used by the tests can be found in the ```test_configurations``` folder inside the ```tests_python``` folder.

### JavaScript tests

The JavaScript tests are written in Jest. They are run as follows:

```bash
npx jest -- tests_javascript
```

### Accessibility tests

The accessibility tests are written in Jest and use Pa11y. The flask application must be running at ```http://localhost:5001``` for these tests to run successfully. They are run as follows:

```bash
npx jest -- tests_accessibility
```

## Cookies used on this website

| Provider | Cookie | Purpose | Expiry |
| -------- | ------ | ------- | ------ |
| This website | session | Used to maintain your session when you are logged into your account on the website | 4 hours |
| This website | cookieMessageApprove | Used to acknowledge acceptance of our cookies policy | 2040 |

## Sample images

A small set of sample images are included for the purposes of evaluating the software.

The Boundary displays on the images are taken from the Office for National Statistics licensed under the Open Government Licence v.3.0 and Contains OS data © Crown copyright and database right 2024. The image tiles used for the maps are provided by ESRI's National Geographic World Map, full attribution is included in each image.

## Troubleshooting

1. The configuration file requires a specific format. Try to follow one of the examples supplied with this project to avoid unexpected problems.
2. When running the **setup** command, the software validates the format of the configuration file. The messages will help you to find any problems with the file.
3. Error **RuntimeError: Application unhealthy state. Please contact the website administrator.**. This means that the website configuration file was modified after the website setup was executed. To fix this problem, run the **Reset command**.

## Contributing

We welcome contributions to the project.

## CI

Please refer to .gitlab-ci.yml for details on the linters and the tests run in the CI workflow.

## Authors and acknowledgment

* Rowland Seymour, The University of Birmingham: Project director.
* Bertrand Perrat, The University of Nottingham: V1 main project contributor.
* Fabián Hernández, The University of Nottingham: V2 main project contributor.
* Catherine Smith, The Research Software Group, part of Advanced Research Computing, University of Birmingham.

The development of this software was supported by a UKRI Future Leaders Fellowship [MR/X034992/1].

## License
<!--- https://gist.github.com/lukas-h/2a5d00690736b4c3a7ba -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
