import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.cart_page import Cart_page
from pages.checkout import Checkout_page
from pages.payment_information_page import Payment_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_confirmation_page import Payment_confirmation_page


@allure.description("Test buy product 1")

def test_buy_product_1(set_up, set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\User\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    base_url = 'https://www.automationexercise.com/login'
    driver.get(base_url)
    driver.maximize_window()
    print("Start Test")

    # Steps:
    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_No_1()

    cp = Cart_page(driver)
    cp.product_confirmation()

    chp = Checkout_page(driver)
    chp.product_confirmation()

    pip = Payment_information_page(driver)
    pip.input_information()

    p = Payment_confirmation_page(driver)
    p.payment_confirmation()

    f = Finish_page(driver)
    f.finish()

    print("Finish Test")
    driver.quit()
