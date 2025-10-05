from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/login")

input_field = driver.find_element(By.CSS_SELECTOR, 'input[id="username"]')
input_field.send_keys("tomsmith")
input_field = driver.find_element(By.CSS_SELECTOR, 'input[id="password"]')
input_field.send_keys("SuperSecretPassword!")
login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
login_button.click()

sleep(5)
driver.quit()
