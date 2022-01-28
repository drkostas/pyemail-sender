from yaml_config_wrapper import Configuration
from typing import *
from io import StringIO, TextIOWrapper
import os


class PyEmailerConfig(Configuration):
    def __init__(self, config_src: Union[TextIOWrapper, StringIO, str],
                 config_schema_path: str = None):
        """ The basic constructor. Creates a new instance of the class.
        :param config_src: The path, file or StringIO object of the configuration to load
        :param config_schema_path: The path, file or StringIO object
                                   of the configuration validation file
        """
        if config_schema_path is None:
            config_schema_path = os.path.join('py_emailer', 'pyemailer_schema.json')
        super().__init__(config_src, config_schema_path)

    def get_pyemailer_config(self, which: int = 0) -> Dict:
        return super().get_config('py-emailer')[which]
