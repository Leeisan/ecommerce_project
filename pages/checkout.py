import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Checkout_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    place_order_button = "//a[@class='btn btn-default check_out']"

    # Getters

    def get_place_order_button(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.place_order_button))))

    # Actions

    def click_proceed_to_checkout_button(self):
        self.get_place_order_button().click()
        print("Click Place Order Button")

    # Methods

    def product_confirmation(self):
        with allure.step("Place Order"):
            Logger.add_start_step(method="place_order")
            self.get_current_url()
            self.click_proceed_to_checkout_button()
            Logger.add_end_step(url=self.driver.current_url, method="place_order")
