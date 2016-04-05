class Page:

    def __init__(self, driver):

        self.driver = driver
        self._search_bar = None
        self._search_result = None
        self._filters_scroller = None

    @property
    def search_bar(self):
        from search_bar import SearchBar

        if self._search_bar is None:
            self._search_bar = SearchBar(self.driver,
                                         self.driver.find_element_by_css_selector(SearchBar.selectors['self']))
        return self._search_bar

    @property
    def search_result(self):
        from search_result import SearchResult

        if self._search_result is None:
            self._search_result = SearchResult(self.driver,
                                               self.driver.find_element_by_class_name(SearchResult.selectors['self']))
        return self._search_result

    @property
    def filters_scroller(self):
        from filters_scroller import FiltersScroller

        if self._filters_scroller is None:
            self._filters_scroller = FiltersScroller(self.driver, self.driver.find_element_by_class_name(FiltersScroller.selectors['self']))
        return self._filters_scroller

    def open(self, url):
        self.driver.get(url)