class PersonalPage:
    def __init__(self, driver):
        self.driver = driver
        self._name = None

    @property
    def name(self):
        from helpers.pages.PersonalPage.personal_page import PersonalPage

        if self._name is None:
            self._name = PersonalPage(self.driver, self.driver.find_element_by_class_name(
                PersonalPage.selectors["self"]))
        return self._name
