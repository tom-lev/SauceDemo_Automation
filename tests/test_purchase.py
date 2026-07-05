from time import sleep
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage



# ה-Fixture שמנהל את חיי הדפדפן
# ה-Fixture המקורי שמנהל את חיי הדפדפן
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    
    options.add_argument("--password-store=basic")
    options.add_experimental_option("prefs", {
        "profile.password_manager_leak_detection": False
    })
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()    # פונקציית הטסט עצמה

def test_complete_purchase(driver):
    # 1. ניווט לאתר
    driver.get("https://www.saucedemo.com")
    
    # 2. יצירת אובייקט של דף הלוגין
    login_page = LoginPage(driver)
    
    # 3. ביצוע הלוגין בפועל
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    
    # 4. בדיקה זמנית שהתחברנו בהצלחה
    assert "inventory.html" in driver.current_url

    inventory_page = InventoryPage(driver)

    inventory_page.click_add_to_cart()
    inventory_page.click_cart_icon()

    cart_page = CartPage(driver)
    assert cart_page.get_item_name() == "Sauce Labs Backpack"
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.enter_first_name("John")
    checkout_page.enter_last_name("Doe")
    checkout_page.enter_postal_code("12345")
    checkout_page.click_continue()
    checkout_page.click_finish()

    assert checkout_page.get_complete_header_text() == "Thank you for your order!"
    sleep(7)  # המתנה של 7 שניות כדי לראות את התוצאה לפני סגירת הדפדפן
