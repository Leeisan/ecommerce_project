import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Payment_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    name_on_card = "//input[@name='name_on_card']"
    card_number = "//input[@name='card_number']"
    cvc = "//input[@name='cvc']"
    expiration_mm = "//input[@name='expiry_month']"
    expiration_yyyy = "//input[@name='expiry_year']"
    pay_button = "//button[@id='submit']"

    # Getters
    def get_name_on_card(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.name_on_card))))

    def get_card_number(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.card_number))))

    def get_cvc(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.cvc))))

    def get_expiration_mm(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.expiration_mm))))

    def get_expiration_yyyy(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.expiration_yyyy))))

    def get_pay_button(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.pay_button))))


    # Actions

    def input_name_on_card(self, name_on_card):
        self.get_name_on_card().send_keys(name_on_card)
        print("Input Name on Card")

    def input_card_number(self, card_number):
        self.get_card_number().send_keys(card_number)
        print("Input Card Number")

    def input_cvc(self, cvc):
        self.get_cvc().send_keys(cvc)
        print("Input CVC")

    def input_expiration_mm(self, expiration_mm):
        self.get_expiration_mm().send_keys(expiration_mm)
        print("Input Expiration Month")

    def input_expiration_yyyy(self, expiration_yyyy):
        self.get_expiration_yyyy().send_keys(expiration_yyyy)
        print("Input Expiration Year")

    def click_pay_button(self):
        self.get_pay_button().click()
        print("Click Pay and Confirm Order Button")


    # Methods

    def input_information(self):
        with allure.step("Input Information"):
            Logger.add_start_step(method="input_information")
            self.get_current_url()
            self.input_name_on_card("Jack")
            self.input_card_number("987654321")
            self.input_cvc("111")
            self.input_expiration_mm("03")
            self.input_expiration_yyyy("2025")
            self.click_pay_button()
            Logger.add_end_step(url=self.driver.current_url, method="input_information")
