from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import TestCase
import unittest


class Test(TestCase):
    """
    Инициализация драйвера:
        1) Зайти на сайт dropbox.com/request и аутентифицироваться
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.dropbox.com/requests")
        email = self.driver.find_element_by_xpath(".//input[@name='login_email']")
        passwd = self.driver.find_element_by_xpath(".//input[@name='login_password']")
        email.send_keys("evgenijkatunov@mail.ru")
        passwd.send_keys("test123")
        passwd.send_keys(Keys.RETURN)

    """
    Тест: Проверка создания запроса файлов
    """

    def test_create_request(self):
        """
        Действия:
            1) Нажать на кнопку создания нового запроса
            2) Ввести описание запрашиваемых файлов
            3) Пройти остальные шаги мастера со значениями по умолчанию
        Проверить:
            Среди запросов есть новый
        """

        self.driver.find_element_by_class_name("drops-grid-create-new-item").click()
        self.driver.find_element_by_name("drops_title").send_keys("TEST1")
        self.driver.find_element_by_class_name("button-primary").click()
        self.driver.find_element_by_class_name("dbmodal-button").click()
        requests = self.driver.find_elements_by_class_name("drops-grid-item-title")
        titles = [request.text for request in requests]
        self.assertIn("TEST1", titles, "Не найдено создаваемого Запроса среди созданных")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main();
