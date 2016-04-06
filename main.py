from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from unittest import TestCase
import unittest

class Test(TestCase):
    """
    Инициализация драйвера:
        1) Заходим на сайт dropbox.com/request и авторизуемся.
    """
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.dropbox.com/requests")
        emails=self.driver.find_elements_by_name("login_email")
        passwds=self.driver.find_elements_by_name("login_password")
        for email in emails:
            if email.is_displayed():
                email.send_keys("evgenijkatunov@mail.ru")
        for passwd in passwds:
            if passwd.is_displayed():
                passwd.send_keys("test123")
                passwd.send_keys(Keys.RETURN)
        while self.driver.current_url!="https://www.dropbox.com/requests":
            self.driver.implicitly_wait(10)

    """
    Тест: Проверка создания запроса файлов
    """
    def test_create_request(self):
        """
        Действия:
            1) Нажать на кнопку создания нового запроса
            2) Ввести описание файла
            3) Пройти остальные шаги мастера со значениями по умолчанию
        Проверить:
            Среди запросов есть новый
        """
        try:
            self.driver.find_element_by_class_name("drops-grid-create-new-item").click()
        except NoSuchElementException:
            self.driver.find_element_by_class_name("button-primary").click()
        self.driver.find_element_by_name("drops_title").send_keys("TEST1")
        self.driver.find_element_by_class_name("button-primary").click()
        link=self.driver.find_element_by_id("drop-link-field").get_attribute("value")
        self.driver.find_element_by_class_name("dbmodal-button").click()
        requests=self.driver.find_elements_by_class_name("drops-grid-item-title")
        titles=[]
        for request in requests:
            titles.append(request.text)
        self.assertIn("TEST1",titles,"Не найдено создаваемого Запроса среди созданных")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main();