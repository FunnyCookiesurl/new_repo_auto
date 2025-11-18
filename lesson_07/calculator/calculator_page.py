from selenium.webdriver.common.by import By


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, 'delay')
        self.screen = (By.CLASS_NAME, 'screen')

    def set_delay(self, seconds):
        input_field = self.driver.find_element(*self.delay_input)
        input_field.clear()
        input_field.send_keys(str(seconds))

    def click_button_7(self):
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()

    def click_button_8(self):
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()

    def click_plus(self):
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()

    def click_equals(self):
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    def get_result(self):
        screen_element = self.driver.find_element(*self.screen)
        return screen_element.text
