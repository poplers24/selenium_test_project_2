
import time
from selenium import webdriver

from pages.cart_page import Cart_page
from pages.login_page import Login_page
from pages.main_page import Main_page


def test_buy_product():
    driver = webdriver.Chrome("/Users/Maksim/Desktop/Python_auto/resource/chromedriver")

    print("\nStart Test")

    login = Login_page(driver)
    login.authorization()
    mp = Main_page(driver)
    mp.select_product()
    cp = Cart_page(driver)
    cp.click_checkout_button()

    time.sleep(10)
    driver.quit()
    print("Browser close")


