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


    def work_with_filters(self, checkboxtitle, asserttext):
        self.page.filters_scroller.check_filter(checkboxtitle)

        text = self.page.search_result.count()
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

if __name__ == '__main__':
    unittest.main()