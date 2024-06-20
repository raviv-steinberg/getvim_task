import pytest

from tests.pages.login_page import LoginPage


@pytest.mark.parametrize("username", ["standard_user"])
def test_standard_user_login(initiate_driver, username):
    login_page = LoginPage(initiate_driver)
    login_page.read_login_password()
    password = login_page.read_login_password()
    login_page.login(username=username, password=password)
    current_url = login_page.get_current_url()
    inventory_url = 'https://www.saucedemo.com/inventory.html'
    assert current_url == inventory_url


@pytest.mark.parametrize("username", ["locked_out_user"])
def test_locked_user_login(initiate_driver, username):
    login_page = LoginPage(initiate_driver)
    login_page.read_login_password()
    password = login_page.read_login_password()
    login_page.login(username=username, password=password)
    error_message = login_page.get_error_message()
    assert error_message == 'Epic sadface: Sorry, this user has been locked out.'
