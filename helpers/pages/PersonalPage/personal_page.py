from helpers.base_component import BaseComponent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PersonalPage(BaseComponent):
    selectors = {
        'self': 'name'
    }

    def get_name(self):
        return self.driver.find_element_by_css_selector('#header-account-menu > span > button > span.name').text

    def click_on_name(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.selectors["self"]))).click()

    def click_logout(self):
        path = "//a [@href='/logout']"
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, path))).click()

