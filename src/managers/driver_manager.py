from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class DriverManager:
    @staticmethod
    def init_driver() -> webdriver.Chrome:
        """
        Initializes and returns a Chrome WebDriver.
        :return: A Chrome WebDriver object initialized with specific options.
        """
        return webdriver.Chrome(
            service=Service(executable_path=DriverManager.get_executable_path()),
            options=DriverManager.get_chrome_options())

    @staticmethod
    def get_chrome_options() -> Options:
        """
        Creates and returns Chrome options for the WebDriver.
        :return: A ChromeOptions object configured with arguments to enhance usability.
        """
        chrome_options = Options()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-extensions")
        return chrome_options

    @staticmethod
    def get_executable_path() -> str:
        """
        Retrieves the executable path for the ChromeDriver.
        :return: The file path of the ChromeDriver executable.
        """
        return ChromeDriverManager().install()
