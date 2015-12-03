from homework7.helpers.base_component import BaseComponent

class SearchResult(BaseComponent):

    selectors = {
        'self': '.gray',
        'button_change': '.change',
        'read_more': '.showTripInfo',
        'text_from': '.from',
        'text_to': '.to',
        'text_date': '.date'
    }

    def click_button_change(self):
        self.driver.find_element_by_css_selector(self.selectors['button_change']).click()

    def read_more(self):
        self.driver.find_element_by_css_selector(self.selectors['read_more']).click()

    def res_from(self):
        return self.driver.find_element_by_css_selector(self.selectors['text_from']).text

    def res_to(self):
        return self.driver.find_element_by_css_selector(self.selectors['text_to']).text

    def res_date(self):
        return self.driver.find_element_by_css_selector(self.selectors['text_date']).text
