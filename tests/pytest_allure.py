import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


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
    def test1(self, ver):
        el = self.driver.find_element(By.XPATH, "//*[@name='q']")
        el.send_keys("Some text")
        el.send_keys(Keys.ENTER)
        if ver > 1:
            assert True
        else:
            with allure.step("Make screen"):
                allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            assert False, "It's not ok"

    @allure.story("Some text2")
    @allure.feature("Open test2")
    @allure.severity("trivial")
    @pytest.mark.parametrize("ver", [1])
    def test2(self, ver):
        # el = self.driver.find_element(By.XPATH, "//*[@name='q']")
        # el.send_keys("Some text")
        # el.send_keys(Keys.ENTER)
        if ver > 1:
            assert True
        else:
            with allure.step("Make screen"):
                allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                              attachment_type=AttachmentType.PNG)
            assert False, "It's not ok"

