class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self._profile = None
        self._passengers = None
        self._contacts = None

    @property
    def profile(self):
        from helpers.pages.ProfileSettings.profile_block import ProfileBlock

        if self._profile is None:
            self._profile = ProfileBlock(self.driver,
                                         self.driver.find_element_by_class_name(ProfileBlock.elements_in_block["self"]))
        return self._profile

    @property
    def passengers(self):
        from helpers.pages.ProfileSettings.passengers_block import PassengersBlock

        if self._passengers is None:
            self._passengers = PassengersBlock(self.driver,
                                               self.driver.find_element_by_class_name(
                                                   PassengersBlock.elements_in_block["self"]))
        return self._passengers

    @property
    def contacts(self):
        from helpers.pages.ProfileSettings.contacts_block import ContactsBlock

        if self._contacts is None:
            self._contacts = ContactsBlock(self.driver,
                                           self.driver.find_element_by_class_name(
                                               ContactsBlock.elements_in_block["self"]))
        return self._contacts
