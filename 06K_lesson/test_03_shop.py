from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://www.saucedemo.com/")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "user-name"))
)

input_field = driver.find_element(By.ID, 'user-name')
input_field.send_keys("standard_user")
input_field = driver.find_element(By.ID, 'password')
input_field.send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.find_element(
    By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(
    By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(
    By.ID, "add-to-cart-sauce-labs-onesie").click()
driver.find_element(
    By.ID, "shopping_cart_container").click()
driver.find_element(
    By.ID, "checkout").click()
input_field = driver.find_element(By.ID, 'first-name')
input_field.send_keys("Алексей")
input_field = driver.find_element(By.ID, 'last-name')
input_field.send_keys("Кравченко")
input_field = driver.find_element(By.ID, 'postal-code')
input_field.send_keys("344000")
driver.find_element(By.ID, "continue").click()

total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
assert "Total: $58.29" in total

driver.quit()
