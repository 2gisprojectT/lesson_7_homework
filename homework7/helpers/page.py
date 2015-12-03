class Page():
    def __init__(self, driver):

        self.driver = driver
        self._window_error = None
        self._search_bar = None
        self._search_result = None

    @property
    def window_error(self):
        from homework7.helpers.window_error import WindowError

        if self._window_error is None:
            self._window_error = WindowError(self.driver, self.driver.find_element_by_css_selector(WindowError.selectors['self']))
        return self._window_error


    @property
    def search_bar(self):
        from homework7.helpers.search_bar import SearchBar

        if self._search_bar is None:
            self._search_bar = SearchBar(self.driver, self.driver.find_element_by_css_selector(SearchBar.selectors['self']))
        return self._search_bar

    @property
    def search_result(self):
        from homework7.helpers.search_result import SearchResult

        if self._search_result is None:
            self._search_result = SearchResult(self.driver, self.driver.find_element_by_css_selector(SearchResult.selectors['self']))
        return self._search_result

    def open(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()

    def search(self, text_from, text_to, date_there, date_back=None):
        from homework7.helpers.search_bar import SearchBar

        self.sb = SearchBar(self.driver)

        self.driver.find_element_by_css_selector(self.sb.selectors['from']).send_keys(text_from)

        self.driver.find_element_by_css_selector(self.sb.selectors['to']).send_keys(text_to)

        template = "//*[contains(@Class," + "'" + date_there + "'" + ")]"
        self.driver.find_element_by_xpath(template).click()

        # можно обойтись без второй даты "обратно"
        if (date_back != None):
            template = "//*[contains(@Class," + "'" + date_back + "'" + ")]"
            self.driver.find_element_by_css_selector(self.sb.selectors['date_back']).click()
            self.driver.find_element_by_xpath(template).click()

        self.driver.find_element_by_css_selector(self.sb.selectors['button']).click()

