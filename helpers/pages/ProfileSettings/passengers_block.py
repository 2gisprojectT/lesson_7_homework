from helpers.base_component import BaseComponent


class PassengersBlock(BaseComponent):
    elements_in_block = {
        "self": "block_passengers",
        "btn_add_passenger": "button_addPassenger",
        "btn_save_passenger": "button_savePassengers"
    }

    def get_add_passenger_btn(self):
        return self.driver.find_element_by_id(self.elements_in_block["btn_add_passenger"])

    def get_save_contacts_btn(self):
        return self.driver.find_element_by_id(self.elements_in_block["btn_save_passenger"])
