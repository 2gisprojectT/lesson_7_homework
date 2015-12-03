from homework7.helpers.base_component import BaseComponent

class SearchBar(BaseComponent):

    selectors = {
        'self': '.layout',
        'from': '.directionFrom div.suggestField input#from0',
        'to': '.directionTo div.suggestField input#to0',
        'date_there': '.dateFrom div.suggestField input#date0',
        'date_back': '.dateTo div.suggestField input#date1',
        'button': '.search input'
    }

    def value_from(self):
       return self.driver.find_element_by_css_selector(self.selectors['from']).get_attribute('value')

    def value_to(self):
       return self.driver.find_element_by_css_selector(self.selectors['to']).get_attribute('value')

    def value_date_there(self):
       return self.driver.find_element_by_css_selector(self.selectors['date_there']).get_attribute('value')

    def value_date_back(self):
       return self.driver.find_element_by_css_selector(self.selectors['date_back']).get_attribute('value')

    def auto_from(self, text_from):
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        self.driver.find_element_by_css_selector(self.selectors['from']).send_keys(text_from)
        WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, self.selectors['from']), 'Новосибирск'))

