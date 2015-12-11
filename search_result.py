from base_component import BaseComponent


class SearchResult(BaseComponent):
    selectors = {
        'self': 'mixedResults__resultsClipper',
        'count': 'mixedResults__header',
        'filters': 'filters__primaryExtended'
    }

    @property
    def count(self):
        return self.driver.find_element_by_class_name(self.selectors['count']).text

    @property
    def filters_open(self):
        return self.driver.find_element_by_class_name(self.selectors['filters']).click()
