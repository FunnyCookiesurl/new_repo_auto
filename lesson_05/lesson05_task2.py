from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Открыть браузер Google Chrome
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

# Открыть сайт http://the-internet.herokuapp.com/inputs/
driver.get("http://the-internet.herokuapp.com/inputs/")


# Кликнуть на синюю кнопку
button = driver.find_element(
    By.CSS_SELECTOR, ".btn.btn-primary")
button.click()


sleep(5)
driver.quit()
