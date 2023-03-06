import allure
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    category_1 = "//*[@id='accordian']/div[2]/div[1]/h4"
    category_2 = "//*[@id='Men']/div/ul/li[1]/a"
    select_product = "//a[@data-product-id='2']"
    cart = "//*[@id='header']/div/div/div/div[2]/div/ul/li[3]/a"

    # Getters

    def get_category_1(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.category_1))))

    def get_category_2(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.category_2))))

    def get_select_product(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.select_product))))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.cart))))

    # Actions

    def click_category_1(self):
        self.get_category_1().click()
        print("Choose Category: Men")

    def click_category_2(self):
        self.get_category_2().click()
        print("Choose Category: T-Shirts")

    def click_select_product(self):
        self.get_select_product().click()
        print("Click Add to Cart")

    def click_cart(self):
        try:
            self.get_cart().click()
            print("Click Cart")
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException")
            self.driver.refresh()
            self.get_cart().click()
            print("Click Cart")

    def select_product_No_1(self):
        with allure.step("Select product No. 1"):
            Logger.add_start_step(method="select_product_No_1")
            self.get_current_url()
            self.click_select_product()
            self.click_cart()
            Logger.add_end_step(url=self.driver.current_url, method="select_product_No_1")
