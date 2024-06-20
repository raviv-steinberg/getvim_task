import pytest

from tests.pages.inventory_page import InventoryPage
from tests.pages.login_page import LoginPage


@pytest.mark.parametrize("username", ["standard_user"])
def test_cart_value_one_item(initiate_driver, username):
    # Log in via standard user.
    login_page = LoginPage(initiate_driver)
    login_page.read_login_password()
    password = login_page.read_login_password()
    login_page.login(username=username, password=password)

    inventory_page = InventoryPage(initiate_driver)
    price = inventory_page.add_random_item()
    cart_value = inventory_page.get_cart_value()
    assert price == cart_value, 'Validation mismatch, Item proce and cart value not equal'
