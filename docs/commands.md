---
id: commands
title: Command Line Interface Reference
sidebar_label: CLI Reference
---

This page is a quick reference for all of the commands that are used to manage the application.

## Setup Command

The `setup` command loads the website configuration and creates the database. It can only be run once (unless the database
is manually deleted). If you need to change a running system then you will need to use the `reset` command instead.

The command is executed by typing:

```bash
flask --debug setup [path_to_configuration]
```

## Reset Command

The `reset` command reloads the website configuration and resets the database after the `setup` command has been run.

This command can be used when:

1. The website configuration file has been modified.
1. The content of the database needs to be deleted and reset.

**Note**: This is a destructive operation that will delete all the database content and any exported files in the
original export location. You will be asked to confirm that you want to run the operation before the script will execute.

The command is executed by typing:

```bash
flask --debug reset [path_to_configuration]
```

## Run Command

The run command starts a test server provided by flask. This should not be used in a production system. The Flask
project provides guidance on [deploying the application in production](https://flask.palletsprojects.com/en/stable/deploying/).

The run command is executed by typing (changing the port number to the port number you want to use):

```bash
flask --debug run --port=5001
```

## Export Command

The database can be exported with the export command. The location where the zip file will be created can be set in the
**exportPathLocation** key in the configuration file.

The data in the database can be exported using the following command. This will export the database as a zip file of
`.csv` files.

```bash
flask --debug export
```

To export to a `.tsv` files rather than `.csv` files the `format` argument can be added to the command.

```bash
flask --debug export --format=tsv
```
