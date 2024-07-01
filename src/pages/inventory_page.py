import random
from typing import List
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from src.common.base_page import BasePage
from selenium import webdriver

MENU_BUTTON = (By.ID, 'react-burger-menu-btn')
LOGOUT_BUTTON = (By.ID, 'logout_sidebar_link')
ALL_ITEMS = (By.CSS_SELECTOR, 'div.inventory_list div.inventory_item')
CART_BUTTON = (By.CSS_SELECTOR, 'div[id=shopping_cart_container] a')
CART_REMOVE_ITEM_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn_secondary.btn_small.cart_button')
CONTINUE_SHOPPING_BUTTON = (By.ID, 'continue-shopping')
INVENTORY_ITEM_PRICE_ELEMENT = (By.CSS_SELECTOR, 'div.inventory_item_price')
CART_ITEMS_PRICE_ELEMENTS = (By.CSS_SELECTOR, 'div.inventory_item_price')


class InventoryPage(BasePage):
    def __init__(self, driver: webdriver):
        """
        Initializes the InventoryPage object with a WebDriver.
        :param driver: The WebDriver instance to interact with the browser.
        """
        super().__init__(driver)

    def open_menu(self) -> None:
        """
        Opens the menu by clicking the menu button.
        :return: None
        """
        self.find_element(
            by_locator=MENU_BUTTON,
            expected_conditions=ec.element_to_be_clickable).click()

    def logout(self) -> None:
        """
        Logs out of the application by clicking the logout button.
        :return: None
        """
        self.find_element(
            by_locator=LOGOUT_BUTTON,
            expected_conditions=ec.element_to_be_clickable).click()

    def get_all_items(self) -> List[WebElement]:
        """
        Retrieves all items from the inventory page.
        :return: A list of WebElement objects representing all items.
        """
        return self.find_elements(
            by_locator=ALL_ITEMS,
            expected_conditions=ec.presence_of_all_elements_located)

    def add_random_item(self) -> float:
        """
        Adds a random item from the inventory to the cart and returns the price of the item.
        :return: The price of the randomly added item.
        """
        self.empty_cart()

        # Go back to shopping page.
        self.find_element(
            by_locator=CONTINUE_SHOPPING_BUTTON,
            expected_conditions=ec.element_to_be_clickable).click()

        # Get all items in inventory.
        items = self.get_all_items()

        # Select random item.
        random_item = random.choice(items)

        # Get the price element.
        price_element = random_item.find_element(By.XPATH, './/div[@class=\'pricebar\']')

        # Get item price.
        price = self.get_price(element=price_element)

        # Add item to cart.
        random_item.find_element(By.CSS_SELECTOR, 'button.btn.btn_primary.btn_small.btn_inventory').click()

        # Return item price.
        return price

    def go_to_cart(self) -> None:
        """
        Navigates to the shopping cart page by clicking the cart button.
        :return: None
        """
        self.find_element(by_locator=CART_BUTTON, expected_conditions=ec.element_to_be_clickable).click()

    def empty_cart(self) -> None:
        """
        Empties the shopping cart by removing all items.
        :return: None
        """
        is_cart_empty = self.is_cart_empty()
        while not is_cart_empty:
            self.get_first_cart_item().click()
            self.driver.refresh()
            is_cart_empty = self.is_cart_empty()

    def is_cart_empty(self) -> bool:
        """
        Checks if the shopping cart is empty.
        :return: True if the cart is empty, False otherwise.
        """
        self.go_to_cart()
        try:
            return len(self.find_elements(
                by_locator=CART_REMOVE_ITEM_BUTTON,
                expected_conditions=ec.visibility_of_all_elements_located,
                wait=5)) == 0
        except TimeoutException:
            return True

    def get_first_cart_item(self) -> WebElement:
        """
        Retrieves the first item in the shopping cart.
        :return: The WebElement representing the first item in the cart.
        """
        return self.find_element(
            by_locator=CART_REMOVE_ITEM_BUTTON,
            expected_conditions=ec.visibility_of_element_located)

    def get_cart_value(self) -> float:
        """
        Calculates the total value of all items in the shopping cart.
        :return: The total value of items in the cart.
        """
        self.go_to_cart()
        res = 0
        items = self.find_elements(
            by_locator=CART_ITEMS_PRICE_ELEMENTS,
            expected_conditions=ec.visibility_of_all_elements_located,
            wait=5)
        for item in items:
            res += self.get_price(element=item)
        return res

    @staticmethod
    def get_price(element: WebElement) -> float:
        """
        Extracts and returns the price from a WebElement representing an item's price.
        :param element: The WebElement containing the item's price.
        :return: The price of the item as a float.
        """
        return float(element.text.split('\n')[0].replace('$', ''))

