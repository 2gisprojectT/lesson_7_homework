from homework7.helpers.base_component import BaseComponent

class WindowError(BaseComponent):

    selectors = {
        'self': '.wide_s',
        'text': '.comment'
    }

    def text_error_read(self):
        return self.driver.find_element_by_css_selector(self.selectors['text']).text
