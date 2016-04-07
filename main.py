from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import TestCase
import unittest
import time


class Test(TestCase):

    def setUp(self):
        """Предусловие: зайти на mail.google.com, аутентифицироваться"""
        self.driver = webdriver.Firefox()
        self.driver.get("https://mail.google.com")
        email = self.driver.find_element_by_name("Email")
        email.send_keys("arch.step.inc@gmail.com")
        email.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(1)
        passw = self.driver.find_element_by_id("Passwd")
        passw.send_keys("testing-1234")
        passw.send_keys(Keys.RETURN)

    def testWritingLetter(self):
        """
            Название: Успешная отправка сообщения
            Шаги: нажать на кнопку "Написать", в открывшемся окне заполнить данные, нажать кнопку "Отправить"
            Результат: в центре окна появилось сообщение об успешной доставке сообщения
        """
        check = "None"
        while check == "None":
            try:
                butt = self.driver.find_element_by_class_name("z0").click()
                check = butt
            except:
                None
        check = "None"
        while check == "None":
            try:
                man = self.driver.find_element_by_name("to").send_keys("arch.step.inc@gmail.com")
                check = man
            except:
                None
        check = "None"
        while check == "None":
            try:
                theme = self.driver.find_element_by_name("subjectbox").send_keys("Приветики")
                check = theme
            except:
                None
        check = "None"
        while check == "None":
            try:
                text = self.driver.find_element_by_class_name("LW-avf").send_keys("Приветики")
                check = text
            except:
                None
        check = "None"
        while check == "None":
            try:
                send = self.driver.find_element_by_id(":mb").click()
                check = send
            except:
                None
        time.sleep(3)
        mes = self.driver.find_element_by_class_name("vh").text
        self.assertEquals(mes, "Письмо отправлено. Просмотреть сообщение", "Damn It!!!")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()