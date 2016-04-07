from selenium import webdriver
from unittest import TestCase
import unittest
import time


class SendGmail(TestCase):
    def sending_mail(self):
        """
         Название :
         Корректная отправка сообщения

         Шаги :
         1. Ввести Email
         2. Нажать "Далее"
         3. Ввести пароль
         4. Нажать "Войти"
         5. Нажать "Написать"
         6. Вввести Email получателя
         7. Ввести текст сообщения
         8. Нажать "Отправить"

         Проверка:
         Выводится сообщение "Письмо отправлено. Просмотреть сообщение"
         """
        driver = webdriver.Firefox()
        driver.get("http://mail.google.com/")

        elem = driver.find_element_by_id("Email")
        elem.send_keys("fedosovdn95@gmail.com")
        elem = driver.find_element_by_id("next")
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_id("Passwd")
        elem.send_keys("plavanye04051995")
        elem = driver.find_element_by_id("signIn")
        elem.click()

        time.sleep(5)
        elem = driver.find_element_by_class_name("z0")
        elem.click()

        time.sleep(2)
        elem = driver.find_element_by_name("to")
        elem.send_keys("Arch.step.inc@gmail.com")
        time.sleep(2)
        elem = driver.find_element_by_id(":iq")
        elem.send_keys("Hello, man!")
        time.sleep(1)
        driver.find_element_by_id(":hb").click()

        time.sleep(2)
        val = driver.find_element_by_class_name("vh").text
        self.assertEqual(val,"Письмо отправлено. Просмотреть сообщение")
        driver.quit()


if __name__ == '__main__':
    unittest.main()
