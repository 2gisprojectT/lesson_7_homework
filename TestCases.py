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

        self.work_with_filters('has_site', '621 организация')

    def test_has_photos(self):
        """
        Steps:
        1. нажать фильтр "есть фото"
        Expected result:
        отфильтровываются организации не имеющие фото(их становится меньше)
        """

        self.work_with_filters('has_photo', '102 организации')

    def test_has_card(self):
        """
        Steps:
        1. нажать фильтр "расчет по картам"
        Expected result:
        отфильтровываются организации не имеющие расчета по картам(их становится меньше)
        """

        self.work_with_filters('has_card', '263 организации')

    def test_work_all_time(self):
        """
        Steps:
        1. нажать фильтр "круглосуточно"
        Expected result:
        отфильтровываются организации не работающие круглосуточно(их становится меньше)
        """

        self.work_with_filters('work_all_time', '13 организаций')

    def test_work_select_time(self):
        """
        Steps:
        1. нажать фильтр "В указанное время"
        2. выбрать день недели(выбран вторник)
        3. выбрать время (выбрано 20 часов)
        Expected result:
        отфильтровываются организации не работающие в данное время(их становится меньше)
        """

        self.work_with_filters('work_select_time', '193 организации', 'Вт', 20)

if __name__ == '__main__':
    unittest.main()