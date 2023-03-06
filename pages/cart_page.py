import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    proceed_to_checkout_button = "//a[@class='btn btn-default check_out']"

    # Getters

    def get_proceed_to_checkout_button(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.proceed_to_checkout_button))))


    # Actions

    def click_proceed_to_checkout_button(self):
        self.get_proceed_to_checkout_button().click()
        print("Click Proceed To Checkout Button")


    # Methods

    def product_confirmation(self):
        with allure.step("Product confirmation"):
            Logger.add_start_step(method="product_confirmation")
            self.get_current_url()
            self.click_proceed_to_checkout_button()
            Logger.add_end_step(url=self.driver.current_url, method="product_confirmation")
