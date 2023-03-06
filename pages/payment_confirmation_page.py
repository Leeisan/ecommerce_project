import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Payment_confirmation_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    continue_button = "//a[@data-qa='continue-button']"

    # Getters

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.continue_button))))

    # Actions

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click Continue Button")

    # Methods

    def payment_confirmation(self):
        with allure.step("Payment Confirmation"):
            Logger.add_start_step(method="payment_confirmation")
            self.get_current_url()
            self.click_continue_button()
            Logger.add_end_step(url=self.driver.current_url, method="payment_confirmation")
