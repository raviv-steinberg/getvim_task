import yaml
import os
from src.utils.Project import Project

FILE_NAME = 'config.yaml'


class ConfigManager:
    def __init__(self):
        root = os.path.join(Project.get_rootpath(), FILE_NAME)
        self.config_file = os.path.join(Project.get_rootpath(), FILE_NAME)
        self.config = self._load_config()

    def _load_config(self):
        with open(self.config_file, 'r') as file:
            return yaml.safe_load(file)

    def get_url(self) -> str:
        return self.config.get('settings', {}).get('url', '')

