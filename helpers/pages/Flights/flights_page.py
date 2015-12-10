class FlightsPage:
    def __init__(self, driver):
        self.driver = driver
        self._spreader = None
        self._enter = None

    @property
    def spreader(self):
        from helpers.pages.Flights.spreader_block import SpreaderBlock

        if self._spreader is None:
            self._spreader = SpreaderBlock(self.driver,
                                           self.driver.find_element_by_class_name(
                                               SpreaderBlock.elements_in_block["self"]))
        return self._spreader

    @property
    def enter(self):
        from helpers.pages.Flights.profile_form_block import ProfileFormBlock

        if self._enter is None:
            self._enter = ProfileFormBlock(self.driver, self.driver.find_element_by_class_name(
                ProfileFormBlock.elements_in_block["self"]))
        return self._enter
