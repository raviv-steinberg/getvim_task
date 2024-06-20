import pytest

from src.managers.config_manager import ConfigManager
from src.managers.driver_manager import DriverManager


@pytest.fixture(scope='session')
def initiate_config():
    yield ConfigManager()


@pytest.fixture(scope='function')
def initiate_driver(initiate_config):
    driver = DriverManager.init_driver()
    driver.get(initiate_config.get_url())
    yield driver
    driver.quit()
