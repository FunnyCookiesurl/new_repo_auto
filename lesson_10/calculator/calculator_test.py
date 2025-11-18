import allure
from selenium import webdriver
from calculator_page import CalculatorPage
from time import sleep

sait = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"


@allure.title("Тест калькулятора с задержкой")
@allure.description(
    "Проверяем что калькулятор корректно работает с задержкой вычислений")
@allure.feature("Калькулятор")
@allure.severity("critical")
def test_calculator():
    with allure.step("Открываем браузер и переходим на страницу калькулятора"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(sait)

    calculator = CalculatorPage(driver)

    with allure.step("Устанавливаем задержку и выполняем вычисление 7 + 8"):
        calculator.set_delay(45)
        calculator.click_button_7()
        calculator.click_plus()
        calculator.click_button_8()
        calculator.click_equals()

    with allure.step("Ждем завершения вычислений"):
        sleep(46)

    with allure.step("Проверяем результат вычислений"):
        result = calculator.get_result()
        assert result == "15", f"Ожидался результат 15, но получили {result}"

    print("Результат: " + result)

    driver.quit()
