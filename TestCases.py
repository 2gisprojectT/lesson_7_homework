#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from page import Page



class SeleniumTest(TestCase):
    """
    Test Cases:
    Проверка фильтров организаций
    """

<<<<<<< HEAD
    def slide_move(self, hour, slider):
        """
        :param hour:  час, на который нужно передвинуть слайдер
        :param slider: сам слайдер
        :return: значение в px, на которое нужно сдвинуть слайдер
        340 - ширина слайдера
        """

        position = slider.get_attribute('style')
        length = len(position)
        position = float(position[6:length - 2])
        return 340 * (hour / 24 - position / 100)

=======
>>>>>>> WIP
    def setUp(self):
        """
        Preconditions:
        1. Находиться на сайте 2gis.ru
        2. Зайти в рубрику
        3. Зайти в фильтры рубрики
        """

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.page = Page(self.driver)
        self.page.open("http://2gis.ru")
        self.page.search_bar.search('компьютеры')
        self.page.search_result.filters_open()

    def tearDown(self):
        self.driver.quit()

    def work_with_filters(self, filter_xpath, asserttext, day=None, hour=None):
        filt = self.driver.find_element_by_xpath(filter_xpath)
        if not filt.is_selected():
            filt.click()

        if 0 < day < 8 and filter_xpath == "//label[@class='radiogroup__label'][3]":
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'dataViewer__frames')))
            self.driver.find_element_by_xpath("//div[@class='radiogroup _week']/label[" + str(day) + "]").click()
        if -1 < hour < 25 and filter_xpath == "//label[@class='radiogroup__label'][3]":
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'dataViewer__frames')))
            action = ActionChains(self.driver)
            action.drag_and_drop_by_offset(self.driver.find_element_by_class_name('filters__raderRunnerIn'),
                                           self.slide_move(hour, self.driver.find_element_by_class_name('filters__raderRunner')), 0).perform()

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'dataViewer__frames')))
        text = self.driver.find_element_by_class_name('mixedResults__header').text
        self.assertEqual(asserttext, text)

    def work_with_filters(self, filter_name, asserttext, day=None, hour=None):
        self.page.filters_scroller.check_filter(filter_name)

        if day is not None and filter_name == 'work_select_time':
            self.page.search_result.wait_load()
            self.page.filters_scroller.select_day(day)
        if -1 < hour < 25 and filter_name == 'work_select_time':
            self.page.search_result.wait_load()
            self.page.filters_scroller.select_hour(hour)

        self.page.search_result.wait_load()
        text = self.page.search_result.counter()
        self.assertEqual(asserttext, text)

    def test_has_site(self):
        """
        Steps:
        1. нажать фильтр "есть сайт"
        Expected result:
        отфильтровываются организации не имеющие сайта(их становится меньше)
        """

<<<<<<< HEAD
        self.work_with_filters("//label[@class='checkbox' and @title='Есть сайт']", '621 организация')
=======
        self.work_with_filters('has_site', '621 организация')
>>>>>>> WIP

    def test_has_photos(self):
        """
        Steps:
        1. нажать фильтр "есть фото"
        Expected result:
        отфильтровываются организации не имеющие фото(их становится меньше)
        """

<<<<<<< HEAD
        self.work_with_filters("//label[@class='checkbox' and @title='Есть фото']", '102 организации')
=======
        self.work_with_filters('has_photo', '102 организации')
>>>>>>> WIP

    def test_has_card(self):
        """
        Steps:
        1. нажать фильтр "расчет по картам"
        Expected result:
        отфильтровываются организации не имеющие расчета по картам(их становится меньше)
        """

<<<<<<< HEAD
        self.work_with_filters("//label[@class='checkbox' and @title='Расчет по картам']", '263 организации')
=======
        self.work_with_filters('has_card', '263 организации')
>>>>>>> WIP

    def test_work_all_time(self):
        """
        Steps:
        1. нажать фильтр "круглосуточно"
        Expected result:
        отфильтровываются организации не работающие круглосуточно(их становится меньше)
        """

<<<<<<< HEAD
        self.work_with_filters("//label[@class='radiogroup__label'][2]", '13 организаций')
=======
        self.work_with_filters('work_all_time', '13 организаций')
>>>>>>> WIP

    def test_work_select_time(self):
        """
        Steps:
        1. нажать фильтр "В указанное время"
        2. выбрать день недели(выбран вторник)
        3. выбрать время (выбрано 20 часов)
        Expected result:
        отфильтровываются организации не работающие в данное время(их становится меньше)
        """

<<<<<<< HEAD
        self.work_with_filters("//label[@class='radiogroup__label'][3]", '192 организации', 2, 20)

if __name__ == "__main__":
    unittest.main()
=======
        self.work_with_filters('work_select_time', '193 организации', 'Вт', 20)

if __name__ == '__main__':
    unittest.main()
>>>>>>> WIP
