import unittest
from unittest import TestCase
from selenium import webdriver
from datetime import datetime, timedelta


class DropboxTest(TestCase):
    def setUp(self):
        """ Предусловие: зайти на сайт dropbox.com, аутентифицироваться """
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.dropbox.com")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("sign-in").click()
        self.driver.find_element_by_xpath(".//input[@name='login_email']").send_keys("testcase.dropbox@mail.ru")
        self.driver.find_element_by_xpath(".//input[@name='login_password']").send_keys("projectT111")
        self.driver.find_element_by_class_name("login-button").click()

    def test_create_request(self):
        """
        Заголовок: позитивный тест создания запроса на файл со сроком загрузки "(текущая дата + 1 день)"
        Шаги
            1. Перейти на страницу "Запросы файлов"
            2. Нажать на кнопку создания нового запроса
            3. Ввести наименование запрашиваемого файла "Тестовый файл"
            4. Не задавать папку для загрузки файла
            5. Включить чекбокс "Добавить срок"
            6. Задать дату (текущая дата+1 день)
            7. Задать время в выпадающем списке "11:00"
        Проверки:
            1. Запрос на файл был создан
            2. Ссылка на запрос файла рабочая
        """
        self.driver.find_element_by_class_name("drops-nav-item").click()
        self.driver.find_element_by_class_name("drops-grid-create-new-item").click()
        self.driver.find_element_by_name("drops_title").send_keys("Тестовый файл")
        self.driver.find_element_by_id("enable-deadlines-checkbox").click()
        self.driver.find_element_by_class_name("c-input").click()
        next_day = datetime.today() + timedelta(days=1)
        self.driver.find_element_by_id("day"+str(next_day.day)+"-"+str(next_day.month-1)).click()
        self.driver.find_element_by_class_name("c-time-selector").click()
        self.driver.find_element_by_xpath(".//div[@title='11:00 ']").click()
        self.driver.find_element_by_class_name("button-primary").click()
        self.link = self.driver.find_element_by_id("drop-link-field").get_attribute("value")
        self.driver.find_element_by_class_name("button-primary").click()
        requests = self.driver.find_elements_by_class_name("drops-grid-item-title")
        self.assertEqual("Тестовый файл", requests[0].text, "Запрос не был создан")
        self.driver.get(self.link)
        info = self.driver.find_element_by_class_name("info__title")
        self.assertEqual("Тестовый файл", info.text, "Ошибка ссылки созданного запроса")

    def tearDown(self):
        """ Завершение сессии """
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
