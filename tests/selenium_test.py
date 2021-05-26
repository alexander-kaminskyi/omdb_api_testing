
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTest:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_test(self):
        self.driver.get("https://www.ukrposhta.ua/ua")
        self.driver.fullscreen_window()
        self.driver.find_element(By.ID, "login-text").click()
        self.driver.find_element(By.XPATH, "//*[@name='login-user']").send_keys("welcome")
        self.driver.find_element(By.XPATH, "//*[@name='pass-user']").send_keys("welcome")
        self.driver.find_element(By.XPATH, "//*[@class='btn btn-primary btn-lg btn-block']").click()
        el = self.driver.find_element(By.XPATH, "//*[@class='text-center alert alert-danger']").text
        expected_err_message = "Невірне ім\'я користувача"
        assert el == expected_err_message

