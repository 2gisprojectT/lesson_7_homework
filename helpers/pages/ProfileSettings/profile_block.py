from helpers.base_component import BaseComponent


class ProfileBlock(BaseComponent):
    elements_in_block = {
        "self": "profile",
        "btn_find_hotels": "hotelCompare",
        "page_title": "pageTitle"
    }

    def get_find_hotels_btn(self):
        return self.driver.find_element_by_id(self.elements_in_block["btn_find_hotels"])

    def get_page_title(self):
        return self.driver.find_element_by_id("pageTitle").text
