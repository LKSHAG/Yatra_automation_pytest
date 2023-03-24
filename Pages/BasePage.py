
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

"""This is the parent of all pages"""
"""It contains all the generic methods and utilities for all pages"""

class BasePage:
    time_delay = 40
    # web_drive_cls = WebDriverWait(self.driver, time_delay)

    def __init__(self,driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, self.time_delay).until(EC.element_to_be_clickable(by_locator)).click()

    def is_alert(self):
        try:
            WebDriverWait(self.driver, self.time_delay).until(EC.alert_is_present())
        except Exception as e:
            print(f"is_alert exception: {e}")

    def do_click_by_javascript(self, by_locator):
        btn = self.driver.find_element(by_locator)
        self.driver.execute_script("arguments[0].click();", btn)

    def do_click_by_xpath(self, by_locator):
        WebDriverWait(self.driver, self.time_delay).until(EC.element_to_be_clickable((By.XPATH, by_locator))).click()

    def do_click_by_index(self, by_locator, index):
        elem = WebDriverWait(self.driver, self.time_delay).until(EC.presence_of_all_elements_located((By.XPATH, by_locator)))
        elem[index].click()

    def do_send_keys(self, by_locator, keys):
        WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_element_located(by_locator)).send_keys(keys)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_element_text_by_xpath(self, by_locator):
        element = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_element_located((By.XPATH, by_locator)))
        return element.text

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_enabled_by_index(self, by_locator, index):
        element = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_all_elements_located(by_locator))
        return bool(element[index])

    def is_invisible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 40).until(EC.invisibility_of_element_located(by_locator))
            return bool(element)
        except Exception as e:
            print(f"is_invisible exception: {e}")

    def is_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return bool(element)
        except Exception as e:
            print(f"is_visible exception: {e}")

    def is_clickable(self, by_locator):
        element = WebDriverWait(self.driver, self.time_delay).until(EC.element_to_be_clickable(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, self.time_delay).until(EC.title_is(title))
        return self.driver.title

    def get_element(self, by_locator):
        element = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_element_located(by_locator))
        return element

    def get_elements(self, by_locator):
        elements = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_all_elements_located(by_locator))
        return elements

    def get_present_element(self, by_locator):
        element = WebDriverWait(self.driver, self.time_delay).until(EC.presence_of_all_elements_located(by_locator))
        return element.text