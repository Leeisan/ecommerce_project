import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get_current_url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method Assert Word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Word Value: Success")

    """Method Screenshot"""
    def get_screenshot(self):
        current_date = datetime.datetime.utcnow().strftime("%y.%m.%d.%H.%M.%S ")
        screenshot_name = 'screenshot' + current_date + '.png'
        self.driver.save_screenshot('C:\\Users\\User\\PycharmProjects\\ecommerce_project\\screen\\' + screenshot_name)

    """Method Assert URL"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("URL Value: Success")
