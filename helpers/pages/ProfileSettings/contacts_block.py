from helpers.base_component import BaseComponent


class ContactsBlock(BaseComponent):
    # описал специально не всё, ибо только для 5 тестов нужные поля
    elements_in_block = {
        "self": "block_contacts",
        "field_email": "email",
        "field_last_name": "input_lastName",
        "selected_country": "country",
        "btn_save_contact": "button_saveContacts"
    }

    def get_user_last_name_field(self):
        return self.driver.find_element_by_id(self.elements_in_block["field_last_name"])

    def get_user_last_name_value(self):
        return self.get_user_last_name_field().get_attribute("value")

    def get_user_email_field(self):
        return self.driver.find_element_by_class_name(self.elements_in_block["field_email"])

    def get_user_selected_country_field(self):
        return self.driver.find_element_by_name(self.elements_in_block["selected_country"])

    def get_user_selected_country_value(self):
        return self.get_user_selected_country_field().get_attribute("value")

    def get_save_contacts_btn(self):
        return self.driver.find_element_by_id(self.elements_in_block["btn_save_contact"])
