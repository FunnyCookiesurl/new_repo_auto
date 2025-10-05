from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Открыть браузер Google Chrome
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

# Открыть сайт http://uitestingplayground.com/classattr/
driver.get("http://uitestingplayground.com/classattr/")


# Кликнуть на синюю кнопку
button = driver.find_element(
    By.CSS_SELECTOR, ".btn-primary.btn-test")
button.click()
alert = driver.switch_to.alert
alert.accept()


sleep(5)
driver.quit()
