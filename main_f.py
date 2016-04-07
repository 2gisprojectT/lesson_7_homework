from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import TestCase
import unittest

class RegisterTest(TestCase):
    def setUp(self):
        self.login = "videlle@mail.ru"
        self.password = "drowssap"
        self.name = ["Name", "Surname"]
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.dropbox.com")
        button_sign_in = self.driver.find_element_by_id("sign-in").click()
        input_login = self.driver.find_element_by_class_name("text-input-input").send_keys(self.login)
        input_password = self.driver.find_element_by_class_name("password-input").send_keys(self.password)
        button_enter = self.driver.find_element_by_class_name("login-button").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_class_name("avatar-wrapper").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_class_name("standalone").click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)

    def test_edit_name(self):
        """
        Шаги воспроизведения:
            1. Войти в свой аккаунт с имеющимися логином и паролем
            2. Зайти в настройки
            3. В открывшемся окне нажать кнопку "Изменить" напротив имени и фамилии
            4. Ввести новые данные и нажать "Сохранить изменения"
            5. Проверить обновленные имя и фамилию
        Ожидаемый результат:
            Имя и фамилия совпадают с введенными
        """
        driver = self.driver
        button_edit = driver.find_element_by_id("edit-name-button").click()
        input_name = driver.find_elements_by_class_name("text-input-input")
        input_name[0].send_keys(self.name[0])
        input_name[1].send_keys(self.name[1])
        button_accept = driver.find_element_by_class_name("dbmodal-button").click()
        name_label = driver.find_element_by_id("name-label")
        self.assertEqual(str(self.name[0]) + " " + str(self.name[1]), name_label.text, "Неверно изменены имя и фамилия")

    def tearDown(self):
         self.driver.quit()

if __name__ == '__main__':
    unittest.main()