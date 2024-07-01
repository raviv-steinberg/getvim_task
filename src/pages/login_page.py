import time
from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.common.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec

LOGIN_CREDENTIALS = (By.ID, 'login_credentials')
PASSWORD_CREDENTIALS = (By.CSS_SELECTOR, 'div.login_password')
USERNAME_TEXTBOX = (By.ID, 'user-name')
PASSWORD_TEXTBOX = (By.ID, 'password')
LOGIN_BUTTON = (By.ID, 'login-button')
ERROR_MESSAGE_ELEMENT = (By.CSS_SELECTOR, 'div.error-message-container.error')


class LoginPage(BasePage):
    def __init__(self, driver: webdriver):
        """
        Initializes the LoginPage object with a WebDriver and the URL of the login page.

        :param driver: The WebDriver instance to interact with the browser.
        """
        super().__init__(driver)

    def read_login_usernames(self) -> List[str]:
        """
        Reads the available login usernames from the login page.
        :return: A list of login usernames.
        """
        credentials = self.find_element(
            by_locator=LOGIN_CREDENTIALS,
            expected_conditions=ec.presence_of_element_located)
        return credentials.text.split('\n')[1:]

    def read_login_password(self) -> str:
        """
        Reads the login password from the login page.
        :return: The login password as a string.
        """
        return self.find_element(
            by_locator=PASSWORD_CREDENTIALS,
            expected_conditions=ec.presence_of_element_located).text.split('\n')[1:][0]

    def login(self, username: str, password: str) -> None:
        """
        Logs in to the application using the provided username and password.
        :param username: The username to log in with.
        :param password: The password to log in with.
        :return: None
        """
        # Insert username.
        self.enter_text(USERNAME_TEXTBOX, username)
        time.sleep(1)

        # Insert password.
        self.enter_text(PASSWORD_TEXTBOX, password)
        time.sleep(1)

        # Click login.
        self.click(LOGIN_BUTTON)
        time.sleep(1)

    def get_current_url(self) -> str:
        """
        Gets the current URL of the browser.
        :return: The current URL as a string.
        """
        return self.driver.current_url

    def get_error_message(self) -> str:
        """
        Retrieves the error message displayed on the login page.
        :return: The error message as a string.
        """
        return self.find_element(
            by_locator=ERROR_MESSAGE_ELEMENT,
            expected_conditions=ec.presence_of_element_located).text
