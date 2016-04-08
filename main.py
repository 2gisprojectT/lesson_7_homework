import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestGmailFailPassMsg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://mail.google.com/")
        self.driver.implicitly_wait(5)

    def test_pass(self):
        """
        Название :
        Провека вывода ошибки при неверном вводе пароля
        Шаги :
        1. Ввести верный Email
        2. Нажать enter
        3. Ввести пароль
        4. Нажать enter
        Тест пройден:
        Выводится сообщение "Указан неправильный адрес или пароль"
        """
        email = self.driver.find_element_by_name("Email")
        email.send_keys("doctorvra4@gmail.com")
        email.send_keys(Keys.RETURN)
        passwd = self.driver.find_element_by_name("Passwd")
        passwd.send_keys("123")
        passwd.submit()
        self.assertTrue("Указан неправильный адрес или пароль" in self.driver.page_source)

    def tearDown(self):
        self.driver.quit()
