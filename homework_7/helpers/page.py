class Page():
    def __init__(self, driver):

        self.driver = driver
        self._registration_window = None

    @property
    def registration(self):
        from homework_7.helpers.registration_form import RegistrationWindow

        if self._registration_window is None:
            self._registration_window = RegistrationWindow(self.driver, self.driver.find_element_by_css_selector(RegistrationWindow.selectors['self']))
        return self._registration_window


    def open(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()