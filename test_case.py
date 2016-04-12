from selenium import webdriver
from unittest import TestCase
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SendGmail(TestCase):
    """
        Корректная отправка сообщения
    """

    def setUp(self):
        """
        Предусловия:
        1. Ввести Email
         2. Нажать "Далее"
         3. Ввести пароль
         4. Нажать "Войти"
        """
        self.driver = webdriver.Firefox()
        self.driver.get("http://mail.google.com/")

        elem = self.driver.find_element_by_id("Email")
        elem.send_keys("fedosovdn95@gmail.com")
        elem = self.driver.find_element_by_id("next")
        elem.click()
        self.wait = WebDriverWait(self.driver, 10)
        elem = self.wait.until(EC.presence_of_element_located((By.ID, "Passwd")))
        elem.send_keys("plavanye04051995")
        elem = self.driver.find_element_by_id("signIn")
        elem.click()


    def test_sending_mail(self):
        """
         Шаги :
         1. Нажать "Написать"
         2. Вввести Email получателя
         3. Ввести текст сообщения
         4. Нажать "Отправить"

         Проверка:
         Выводится сообщение "Письмо отправлено. Просмотреть сообщение"
         """
        elem = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "z0")))
        elem.click()

        elem = self.wait.until(EC.presence_of_element_located((By.NAME, "to")))
        elem.send_keys("Arch.step.inc@gmail.com")
        elem = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "LW-avf")))
        elem.send_keys("Hello, man!")
        elem = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id=":hm"]')))
        elem.click()

        self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "vh"), "Письмо отправлено. Просмотреть сообщение"))


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
