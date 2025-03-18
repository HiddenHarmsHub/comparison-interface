# Comparison Interface V2

This repository provides a web interface to facilitate the collection of comparative judgement data. It offers a 
highly configurable interface which only requires a configuration file and a set of image files as input. 
Data is stored in an SQLite database which is part of the standard python library so no additional database is required. 
There is no restriction regarding the nature of the items that can be compared in the software but it has been used 
previously on geospatial datasets to be processed with the [Bayesian Spatial Bradley--Terry model BSBT](https://github.com/rowlandseymour/BSBT).

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

There is also an option to expose the table containing the decisions made by users (no user details) and the table containing the item details via a secured api. This is enabled by setting the 'API_ACCESS' variable in the ```configuration/flask.py``` file to ```True```. In addition a ```.apikey``` file needs to be created at the top level of the repository. This should contain the secret key which will be used to authenticate api calls. The file name used to store the key can be changed in the ```configuration/flask.py``` file.

