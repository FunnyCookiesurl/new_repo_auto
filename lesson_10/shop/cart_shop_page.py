from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    def __init__(self, driver: WebDriver) -> None:
        """
        Попадаем на страницу корзины.
        """
        self.driver = driver
        self.checkout_button = (By.ID, 'checkout')

    def go_to_checkout(self) -> None:
        """
        Переходим к оформлению заказа.
        """
        self.driver.find_element(*self.checkout_button).click()
