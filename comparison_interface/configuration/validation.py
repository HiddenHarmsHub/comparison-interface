import os

from marshmallow import ValidationError

from .csv_validation import CsvValidator
from .schema import Configuration as ConfigSchema
from .website import Settings as WS


class Validation:
    """A Validator for the config file."""

    def __init__(self, app) -> None:
        """Initialise the Validation with the Flask app."""
        self.__app = app

    def validate(self) -> list:
        """Validate the configuration file or directory."""
        conf = WS.get_configuration(self.__app)
        schema = ConfigSchema()
        try:
            schema.load(conf)
        except ValidationError as err:
            self.__app.logger.critical(err)
            exit()
        #now if we reference a csv file validate that
        if "csvFile" in conf["comparisonConfiguration"]:
            config_location = WS.get_configuration_location(self.__app)
            csv_validator = CsvValidator()
            csv_validator.validate(os.path.join(config_location, conf["comparisonConfiguration"]["csvFile"]))

    def check_config_path(self, path):
        """Check that the path provided meets the requirements.

        The requirements are either a path to a JSON file or a path to a directory containing a single JSON file and
        a CSV file.
        """
        full_path = os.path.abspath(os.path.dirname(__file__)) + "/../" + path
        if os.path.isdir(full_path):
            file_count = 0
            json_file = None
            csv_file = None
            for file in os.listdir(full_path):
                file_count += 1
                if file.lower()[-4:] == ".csv":
                    csv_file = file
                elif file.lower()[-5:] == ".json":
                    json_file = file
            if file_count != 2 or json_file is None or csv_file is None:
                self.__app.logger.critical(
                    "If the config path is to a directory then the directory must contain a JSON file and a CSV file."
                )
                exit()
        elif os.path.isfile(full_path):
            if path.lower()[-5:] != ".json":
                self.__app.logger.critical("If the config path is to a file it must be a .json file.")
                exit()
