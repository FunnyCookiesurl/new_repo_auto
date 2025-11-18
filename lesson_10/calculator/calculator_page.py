from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    def __init__(self, driver: WebDriver) -> None:
        """
        Заходим на страницу калькулятора.
        """
        self.driver = driver
        self.delay_input = (By.ID, 'delay')
        self.screen = (By.CLASS_NAME, 'screen')

    def set_delay(self, seconds: int) -> None:
        """
        Устанавливаем задержку вычислений в секундах.
        """
        input_field = self.driver.find_element(*self.delay_input)
        input_field.clear()
        input_field.send_keys(str(seconds))

    def click_button_7(self) -> None:
        """
        Нажать на кнопку с цифрой 7.
        """
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()

    def click_button_8(self) -> None:
        """
        Нажать на кнопку с цифрой 8.
        """
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()

    def click_plus(self) -> None:
        """
        Нажать на кнопку сложения (+).
        """
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()

    def click_equals(self) -> None:
        """
        Нажать на кнопку равенства (=).
        """
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    def get_result(self) -> str:
        """
        Получаем результат вычислений с экрана калькулятора.
        """
        screen_element = self.driver.find_element(*self.screen)
        return screen_element.text
