from helpers.base_component import BaseComponent


class SpreaderBlock(BaseComponent):
    elements_in_block = {
        "self": "spreader",
        "enter_form": "enter",
        "known_user": "knownUser"
    }

    def login_in_form_click(self):
        self.driver.find_element_by_class_name(self.elements_in_block["enter_form"]).click()

    def known_user_form_click(self):
        self.driver.find_element_by_class_name(self.elements_in_block["known_user"]).click()
