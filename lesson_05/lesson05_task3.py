from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
input_field.send_keys("Sky")
input_field.clear()
input_field.send_keys("Pro")

sleep(5)
driver.quit()
