import unittest
from unittest import TestCase
from selenium import webdriver


class DataInputTest(TestCase):
    def setUp(self):
        """
        Инициализация драйвера для тестирования:
            [1] Заходим на сайт onetwotrip.com под данным логином и паролем.
        """
        email = "antonprojectt@leeching.net"
        password = "test009"

        self.driver = webdriver.Firefox()
        self.driver.get("https://www.onetwotrip.com/ru/")
        self.driver.find_element_by_class_name("enter").click()
        self.driver.find_element_by_id("input_auth_email").send_keys(email)
        self.driver.find_element_by_id("input_auth_pas").send_keys(password)
        self.driver.find_element_by_class_name("pos_but").click()

    def test_name_input(self):
        """
        Шаги воспроизведения:
            [1] Переходим в свой профиль и вводим имя и фамилию в поля "Имя" и "Фамилия".
            [2] Нажимаем кнопку "Сохранить изменения"
            [3] Обновляем страницу браузера.
            [4] Проверяем имя и фамилию в соответствии с ранее введеными.
        Ожидаемый результат:
            [*] Имя и фамилия совпадают с введеными ранее значениями.
        """
        test_data = ["Иван", "Иванов"]

        driver = self.driver
        driver.find_element_by_class_name("knownUser").click()
        driver.implicitly_wait(10)
        input_firstname_field = driver.find_element_by_id("input_firstName")
        input_lastname_field = driver.find_element_by_id("input_lastName")
        save_button = driver.find_element_by_id("button_saveContacts")

        input_firstname_field.clear()
        input_lastname_field.clear()

        input_firstname_field.send_keys(test_data[0])
        input_lastname_field.send_keys(test_data[1])
        save_button.click()
        driver.refresh()

        input_firstname_field = driver.find_element_by_id("input_firstName")
        input_lastname_field = driver.find_element_by_id("input_lastName")

        self.assertEqual(input_firstname_field.get_attribute("value"), test_data[0])
        self.assertEqual(input_lastname_field.get_attribute("value"), test_data[1])

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()