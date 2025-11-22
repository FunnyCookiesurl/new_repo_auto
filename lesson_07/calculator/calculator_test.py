from selenium import webdriver
from calculator_page import CalculatorPage
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

calculator = CalculatorPage(driver)

calculator.set_delay(45)
calculator.click_button_7()
calculator.click_plus()
calculator.click_button_8()
calculator.click_equals()

sleep(46)

result = calculator.get_result()
assert result == "15", f"В окне отобразится результат 15 через 45 секунд {
    result}"

print("Результат: " + result)

driver.quit()
