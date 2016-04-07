from unittest import TestCase
import unittest
from selenium import webdriver

"""
Test Case:
    Проверка поиска организации
Начальные услови:
    1. Находимся на сайте 2gis.ru
Шаги:
    1. Ввести в поле поиска имя организации
    2. Выбрать из списка соответствующую организацию
Ожидаемый результат:
    Открывается карточка организации с соответствующим названием
"""


class SiteTestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get('http://2gis.ru/')

    def tearDown(self):
        self.driver.close()

    def test_bus(self):
        self.driver.find_element_by_class_name('suggest__input').send_keys('СибГУТИ')
        self.driver.find_element_by_class_name('searchBar__submit').click()

        self.driver.find_element_by_class_name('miniCard__headerTitleLink').click()
        text = self.driver.find_element_by_class_name('cardHeader__headerNameText').text
        self.assertEqual('Сибирский государственный университет телекоммуникаций и информатики', text)


if __name__ == "__main__":
    unittest.main()
