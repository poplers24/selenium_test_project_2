
import time
from selenium import webdriver

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


def test_buy_product():
    driver = webdriver.Chrome("/Users/Maksim/Desktop/Python_auto/resource/chromedriver")

    print("\nStart Test")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    cip = Client_information_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.payment()

    f = Finish_page(driver)
    f.finish()

    time.sleep(10)
    driver.quit()
    print("Browser close")


