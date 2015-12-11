from base_component import BaseComponent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from search_result import SearchResult

class FiltersScroller(BaseComponent):

    selectors = {
        'self': 'filters__scroller',
        'has_site': "//label[@class='checkbox' and @title='Есть сайт']",
        'has_foto': "//label[@class='checkbox' and @title='Есть фото']",
        'has_card': "//label[@class='checkbox' and @title='Расчет по картам']",
        'work_all_time': "//div[@class='radiogroup _workTimeModes']/label[2]",
        'wark_select_time': "//div[@class='radiogroup _workTimeModes']/label[3]"
    }

    def check_filter(self, tip):
        checkbox = self.driver.find_element_by_xpath(self.selectors[tip])
        if not checkbox.is_selected():
            checkbox.click()
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, SearchResult.selectors['self'])))

