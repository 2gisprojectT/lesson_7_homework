#-*- coding:UTF-8 -*-

import unittest
from unittest import TestCase
from selenium import webdriver

from homework7.helpers.page import Page

month = {
        '13_дек': '1449943200000',
        '14_дек': '1450029600000',
        '15_дек': '1450116000000',
        '16_дек': '1450202400000',
        '17_дек': '1450288800000',
        '18_дек': '1450375200000',
        '19_дек': '1450461600000',
        '20_дек': '1450548000000'
    }

class FiveTestsComponentPageClass(TestCase):

    def setUp(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        self.page = Page(driver)
        self.page.open("https://www.onetwotrip.com")


    def test_autocomplete(self):
        """ тест первый
        проверка автозаполнения

        заполняем первое поле "откуда", вводим латинскими буквами неполное слово "novos"
        проверяем, чтобы система сама исправила его на "Новосибирск"
        """

        text_from_before = 'novos'
        text_from_after = 'Новосибирск'

        self.page.search_bar.auto_from(text_from_before)

        self.assertEqual(self.page.search_bar.value_from(), text_from_after)


    def test_incorrectly_specified_dates(self):
        """ тест второй
        проверка неверно заданных дат (дата прилета раньше даты вылета)

        попытаемся осуществить поиск (из Новосибирска в Москву, вылет 19 декабря, прилет 18 декабря)
        должно выскочить окошко с предупреждением о том, что даты неверно заданы
        """

        text_from = 'Новосибирск'
        text_to = 'Москва'

        self.page.search(text_from, text_to, month['19_дек'], month['18_дек'])

        text_error = self.page.window_error.text_error_read()
        self.assertEqual(text_error, 'Неверно заданы даты')


    def test_control_data_after_click_button_change(self):
        """ тест третий
        проверка кнопки Изменить

        осуществляем поиск (из Новосибирска в Москву, вылет 13 декабря)
        затем нажимаем на кнопку "Изменить", то есть вернуться к первоначальному запросу
        нужно проверить, что данные в полях сохранились.
        """

        text_from = 'Новосибирск'
        text_to = 'Москва'

        self.page.search(text_from, text_to, month['13_дек'])
        text_date = self.page.search_bar.value_date_there()

        self.page.search_result.click_button_change()

        self.assertEqual(text_from, self.page.search_bar.value_from())
        self.assertEqual(text_to, self.page.search_bar.value_to())
        self.assertEqual(text_date, self.page.search_bar.value_date_there())


    def test_check_result_of_search(self):
        """ тест четвертый
        проверка результата поиска

        осуществляем поиск (из Новосибирска в Москву, вылет 13 декабря)
        затем нажимаем на ссылку "подробнее"
        нужно проверить результаты поиска с введенными ранее данными
        """

        text_from = 'Новосибирск'
        text_to = 'Москва'

        self.page.search(text_from, text_to, month['13_дек'])
        text_date = self.page.search_bar.value_date_there()

        self.page.search_result.read_more()
        res_text_from = self.page.search_result.res_from()
        res_text_to = self.page.search_result.res_to()
        res_text_date = self.page.search_result.res_date()

        self.assertIn(text_from, res_text_from)
        self.assertIn(text_to, res_text_to)
        self.assertEqual(text_date[:2], res_text_date[:2])
        self.assertEqual(text_date[4:6], res_text_date[4:6])


    def test_match_cities_in_field(self):
        """ тест пятый
        проверка невозможности выполнения запроса, в котором названия городов в полях совпадают

        попытаемся осуществить поиск (из Новосибирска в Новосибирск, вылет 13 декабря)
        нужно, чтобы выскочило окно с предупреждением о том, что пункты вылета и прилета совпадают.
        """

        text_from = text_to = 'Новосибирск'

        self.page.search(text_from, text_to, month['13_дек'])

        text_error = self.page.window_error.text_error_read()
        self.assertEqual(text_error, 'Неверно задан маршрут. Совпадают пункты вылета и прилёта.')


    def tearDown(self):
        self.page.close()


if __name__ == '__main__':
    unittest.main()
