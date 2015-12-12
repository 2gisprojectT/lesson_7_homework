from base_component import BaseComponent



class SearchBar(BaseComponent):
    selectors = {
        'self': '.online__searchBar',
        'input': '.suggest__input',
        'submit': '.searchBar__submit'
    }

    def search(self, text):
        self.driver.find_element_by_css_selector(self.selectors['input']).send_keys(text)
        self.driver.find_element_by_css_selector(self.selectors['submit']).click()
