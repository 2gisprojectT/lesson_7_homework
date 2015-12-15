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
        self.driver.close()

    def work_with_filters(self, filter_name, asserttext, day=None, hour=None):


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
        filter_name = 'has_site'
        asserttext = '621 организация'
        self.page.filters_scroller.check_filter(filter_name)

        self.page.search_result.wait_load()
        text = self.page.search_result.counter()
        self.assertEqual(asserttext, text)

    def test_has_photos(self):
        """
        Steps:
        1. нажать фильтр "есть фото"
        Expected result:
        отфильтровываются организации не имеющие фото(их становится меньше)
        """

        filter_name = 'has_photo'
        asserttext = '102 организации'
        self.page.filters_scroller.check_filter(filter_name)

        self.page.search_result.wait_load()
        text = self.page.search_result.counter()
        self.assertEqual(asserttext, text)

    def test_has_card(self):
        """
        Steps:
        1. нажать фильтр "расчет по картам"
        Expected result:
        отфильтровываются организации не имеющие расчета по картам(их становится меньше)
        """

        filter_name = 'has_card'
        asserttext = '263 организации'
        self.page.filters_scroller.check_filter(filter_name)

        self.page.search_result.wait_load()
        text = self.page.search_result.counter()
        self.assertEqual(asserttext, text)

    def test_work_all_time(self):
        """
        Steps:
        1. нажать фильтр "круглосуточно"
        Expected result:
        отфильтровываются организации не работающие круглосуточно(их становится меньше)
        """

        filter_name = 'work_all_time'
        asserttext = '13 организаций'
        self.page.filters_scroller.check_filter(filter_name)

        self.page.search_result.wait_load()
        text = self.page.search_result.counter()
        self.assertEqual(asserttext, text)

    def test_work_select_time(self):
        """
        Steps:
        1. нажать фильтр "В указанное время"
        2. выбрать день недели(выбран вторник)
        3. выбрать время (выбрано 20 часов)
        Expected result:
        отфильтровываются организации не работающие в данное время(их становится меньше)
        """

        filter_name = 'work_select_time'
        asserttext = '193 организации'
        day = 'Вт'
        hour = 20
        self.page.filters_scroller.check_filter(filter_name)

        self.page.search_result.wait_load()
        self.page.filters_scroller.select_day(day)

        self.page.search_result.wait_load()
        self.page.filters_scroller.select_hour(hour)

        self.page.search_result.wait_load()
        text = self.page.search_result.counter()
        self.assertEqual(asserttext, text)

if __name__ == '__main__':
    unittest.main()