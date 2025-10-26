from selenium import webdriver
from login_shop_page import LoginPage
from shop_main import MainPage
from cart_shop_page import CartPage
from checkout_shop_page import CheckoutPage


driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    main_page = MainPage(driver)
    main_page.add_products_to_cart()
    main_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.go_to_checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form("Алексей", "Кравченко", "344000")
    total = checkout_page.get_total_amount()
    assert "$58.29" in total, f"Ожидалось '$58.29', но получили '{total}'"

    print("Итоговая сумма: " + total)

finally:
    driver.quit()
