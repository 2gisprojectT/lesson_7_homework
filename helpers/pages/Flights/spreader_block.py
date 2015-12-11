from helpers.base_component import BaseComponent


class SpreaderBlock(BaseComponent):
    elements_in_block = {
        "self": "spreader",
        "enter_form": "enter",
        "known_user": "knownUser"
    }

    def go_to_login_form(self):
        self.driver.find_element_by_class_name(self.elements_in_block["enter_form"]).click()

    def go_to_known_user_form(self):
        self.driver.find_element_by_class_name(self.elements_in_block["known_user"]).click()
