import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.google.com")

    def teardown(self):
        self.driver.quit()

    @allure.story("Some text")
    @allure.feature("Open pages")
    @allure.severity("blocker")
    @pytest.mark.parametrize("ver", [1, 2, 3])
    def test(self, ver):
        if ver > 1:
            assert True
        else:
            with allure.step("Make screen"):
                allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            assert False, "It's not ok"

