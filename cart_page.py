
from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_item_name = (By.CLASS_NAME, "inventory_item_name")
        self.checkout_button = (By.ID, "checkout")


    def get_item_name(self):
        return self.driver.find_element(*self.inventory_item_name).text
    
    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()


