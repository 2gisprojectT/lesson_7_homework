'''
Тест-кейс "Ввод текста, не являющегося Email-адресом"
Шаги:
  1. Зайти на сайт "mail.google.com"
  2. Нажать "Нужна помощь?"
  3. Выбрать вариант "При входе в систему возникают другие проблемы"
  4. В открывшемся текстовом поле набрать любой текст, не являющийся Email-адресом
     (В данном тест-кейсе "This is not Email")
Ожидание:
  Вывод сообщения об ошибке "Введите действительный адрес электронной почты." в браузере,
  программа выдает сообщение "Тест завершен успешно"
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class auto_test_Gmail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://mail.google.com")
        self.driver.implicitly_wait(5)

    def test_wrong_email(self):
        key_help = self.driver.find_element_by_class_name("need-help")
        key_help.send_keys(Keys.RETURN)
        radio = self.driver.find_element_by_css_selector("input[type='radio'][value='3']")
        radio.click()
        email = self.driver.find_element_by_css_selector("[name='Email2']")
        email.send_keys("This is not Email")
        email.submit()
        self.assertIn("Введите действительный адрес электронной почты.",self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

