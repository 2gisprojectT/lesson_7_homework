from selenium.webdriver.support.select import Select

from helpers.base_component import BaseComponent


class ContactsBlock(BaseComponent):
    elements_in_block = {
        "self": "block_contacts",
        "field_email": "email",
        "field_last_name": "input_lastName",
        "selected_country": "country",
        "btn_save_contact": "button_saveContacts"
    }

    def get_user_first_name_field(self):
        return self.driver.find_element_by_id(self.elements_in_block["field_last_name"])

    def get_user_first_name_value(self):
        return self.get_user_first_name_field().get_attribute("value")

    def get_user_email_field(self):
        return self.driver.find_element_by_class_name(self.elements_in_block["field_email"])

    def get_user_email_text(self):
        return self.get_user_email_field().text

    def get_user_selected_country_field(self):
        return self.driver.find_element_by_name(self.elements_in_block["selected_country"])

    def get_user_selected_country_value(self):
        return self.get_user_selected_country_field().get_attribute("value")

    def get_save_contacts_btn(self):
        return self.driver.find_element_by_id(self.elements_in_block["btn_save_contact"])

    def input_first_name(self, user_first_name):
        self.get_user_first_name_field().send_keys(user_first_name)
        self.get_save_contacts_btn().click()

    def select_user_country(self, user_country):
        Select(self.get_user_selected_country_field()).select_by_value(user_country.get(u"Сингапур"))