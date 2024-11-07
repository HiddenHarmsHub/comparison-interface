from marshmallow import ValidationError

from .schema import Configuration as ConfigSchema
from .website import Settings as WS


class Validation:
    """A Validator for the config file."""

    def __init__(self, app) -> None:
        """Initialise the Validation with the Flask app."""
        self.__app = app

    def validate(self) -> list:
        """Validate the configuration file."""
        conf = WS.get_configuration(self.__app)
        schema = ConfigSchema()
        try:
            schema.load(conf)
        except ValidationError as err:
            self.__app.logger.critical(err)
            exit()
