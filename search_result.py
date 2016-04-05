from base_component import BaseComponent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SearchResult(BaseComponent):
    selectors = {
        'self': 'mixedResults__resultsClipper',
        'count': 'mixedResults__header',
        'filters': 'filters__primaryExtended'
    }

    def counter(self):
        return self.driver.find_element_by_class_name(self.selectors['count']).text

    def filters_open(self):
        self.driver.find_element_by_class_name(self.selectors['filters']).click()

    def wait_load(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, self.selectors['self'])))