import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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


class Test_2gis_Selenium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://mail.google.com/")
        self.driver.implicitly_wait(5)

    def test_pass(self):
        elem = self.driver.find_element_by_name("Email")
        elem.send_keys("doctorvra4@gmail.com")
        elem.send_keys(Keys.RETURN)
        elem1 = self.driver.find_element_by_name("Passwd")
        elem1.send_keys("123")
        elem1.send_keys(Keys.RETURN)
        assert "Указан неправильный адрес или пароль" in self.driver.page_source
        print("Тест пройден")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main
