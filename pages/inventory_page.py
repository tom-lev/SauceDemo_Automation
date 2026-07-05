from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.Add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.Cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def click_add_to_cart(self):
        self.driver.find_element(*self.Add_to_cart_button).click()

    def click_cart_icon(self):
        self.driver.find_element(*self.Cart_icon).click()

