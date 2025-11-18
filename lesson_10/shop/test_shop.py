import allure
from selenium import webdriver
from login_shop_page import LoginPage
from shop_main import MainPage
from cart_shop_page import CartPage
from checkout_shop_page import CheckoutPage


@allure.title("Тест интернет-магазина")
@allure.description("Проверяем полный цикл покупки в интернет-магазине")
@allure.feature("Магазин")
@allure.severity("critical")
def test_shop():
    with allure.step("Открываем браузер и переходим на сайт магазина"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

    try:
        with allure.step("Выполняем авторизацию"):
            login_page = LoginPage(driver)
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавляем товары в корзину"):
            main_page = MainPage(driver)
            main_page.add_products_to_cart()
            main_page.go_to_cart()

        with allure.step("Переходим к оформлению заказа"):
            cart_page = CartPage(driver)
            cart_page.go_to_checkout()

        with allure.step("Заполняем данные для оформления"):
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_checkout_form("Алексей", "Кравченко", "344000")

        with allure.step("Проверяем итоговую сумму"):
            total = checkout_page.get_total_amount()
            assert "$58.29" in total, f"Ожидалось '$58.29', но получили '{
                total}'"

        print("Итоговая сумма: " + total)

    finally:
        driver.quit()
