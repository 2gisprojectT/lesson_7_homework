import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import TestCase


class Test(TestCase):
    def setUp(self):
        """
        Начальные условия:
            1) Переходим на страницу mail.google.com
            2) Авторизируемся через логин и пароль
        """
        email = "2giskargapolovtest@gmail.com"
        passwd = "2GisKargapolovTestTest"
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get("http://mail.google.com/")
        self.driver.find_element_by_id("Email").send_keys(email)
        self.driver.find_element_by_id("next").click()
        self.driver.find_element_by_id("Passwd").send_keys(passwd)
        self.driver.find_element_by_id("signIn").click()

    def test_new_test(self):
        """
        Шаги воспроизведения:
            1)Ввести в форму поиска текст, которого нет в письмах ящика.
            2)Нажать Enter.
        Ожидаемый результат:
            Вывод сообщения о том, что писем с таким текстом в ящике не найдено.
        """
        search_text = "some_text"
        self.driver.find_element_by_id("gbqfq").send_keys(search_text + Keys.RETURN)
        self.assertIn("Писем не найдено.",self.driver.page_source)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main
