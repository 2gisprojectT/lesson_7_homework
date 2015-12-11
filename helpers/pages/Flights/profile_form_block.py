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

    def login_in(self, user_email, user_password):
        register_email_field = self.get_login_email_field()
        register_password_field = self.get_login_password_field()

        register_email_field.send_keys(user_email)
        register_password_field.send_keys(user_password)

        self.get_login_in_btn().click()

