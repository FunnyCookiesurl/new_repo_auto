from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, 'user-name')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')

    def login(self, username, password):
        login_data = {
            'user-name': username,
            'password': password
        }

        for field_id, value in login_data.items():
            input_field = self.driver.find_element(By.ID, field_id)
            input_field.send_keys(value)

        self.driver.find_element(By.ID, "login-button").click()
