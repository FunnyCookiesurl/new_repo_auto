from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    def __init__(self, driver: WebDriver) -> None:
        """
        Попадаем на страницу оформления заказа.
        """
        self.driver = driver
        self.first_name_field = (By.ID, 'first-name')
        self.last_name_field = (By.ID, 'last-name')
        self.postal_code_field = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')
        self.total_amount = (By.CSS_SELECTOR, '.summary_total_label')

    def fill_checkout_form(
            self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняем форму оформления заказа.
        """
        first_name_element = self.driver.find_element(*self.first_name_field)
        first_name_element.send_keys(first_name)
        last_name_element = self.driver.find_element(*self.last_name_field)
        last_name_element.send_keys(last_name)
        postal_code_element = self.driver.find_element(*self.postal_code_field)
        postal_code_element.send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total_amount(self) -> str:
        """
        Получаем итоговую сумму заказа.
        """
        total_element = self.driver.find_element(*self.total_amount)
        return total_element.text
