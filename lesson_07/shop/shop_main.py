from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_1 = (By.ID, 'add-to-cart-sauce-labs-backpack')
        self.product_2 = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
        self.product_3 = (By.ID, 'add-to-cart-sauce-labs-onesie')
        self.cart_button = (By.ID, 'shopping_cart_container')

    def add_products_to_cart(self):
        self.driver.find_element(*self.product_1).click()
        self.driver.find_element(*self.product_2).click()
        self.driver.find_element(*self.product_3).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
