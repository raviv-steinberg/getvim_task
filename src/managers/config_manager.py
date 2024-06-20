import yaml
import os
from src.utils.Project import Project

FILE_NAME = 'config.yaml'


class ConfigManager:
    """
    Manages the configuration settings from a YAML file.
    """

    def __init__(self):
        """
        Initializes the ConfigManager by setting the path to the configuration file and loading its content.
        """
        self.config_file = os.path.join(Project.get_rootpath(), FILE_NAME)
        self.config = self._load_config()

    def _load_config(self) -> dict:
        """
        Loads the configuration from the YAML file.
        :return: The loaded configuration data
        """
        with open(self.config_file, 'r') as file:
            return yaml.safe_load(file)

    def get_url(self) -> str:
        """
        Retrieves the URL from the configuration settings.
        :return: The URL from the configuration settings, or an empty string if not found
        """
        return self.config.get('settings', {}).get('url', '')
