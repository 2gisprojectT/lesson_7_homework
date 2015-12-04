from helpers.base_component import BaseComponent


class ProfileFormBlock(BaseComponent):
    elements_in_block = {
        "self": "enter",
        "field_email": "auth_email",
        "field_password": "auth_pas",
        "btn_login_in": "pos_but"
    }

    def get_login_email_field(self):
        return self.driver.find_element_by_name(self.elements_in_block["field_email"])

    def get_login_password_field(self):
        return self.driver.find_element_by_name(self.elements_in_block["field_password"])

    def get_login_in_btn(self):
        return self.driver.find_element_by_class_name(self.elements_in_block["btn_login_in"])
