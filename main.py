from unittest import TestCase
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''
Тест-кейс "Ввод несуществующего email в форме "забыли пароль""
 Шаги:
 1. Зайти на сайт "www.onetwotrip.com"
 2. Нажать "Личный кабинет"
 3. В открывшемся окне нажимаем "забыли пароль"
 4. В открывшемся окне ввести несуществующий email
 +
 Ожидание:
 +  Вывод сообщения об ошибке "Пользователя с таким email не существует" в браузере.
'''


class OttripTest(TestCase):
    driver = webdriver.Firefox()
    driver.get("http://www.onetwotrip.com/ru")
    driver.find_element_by_class_name("enter").click()
    driver.find_element_by_class_name("getNewPas").click()
    even = driver.find_element_by_id("input_remind_email")
    even.send_keys("llllll@mail.ru")
    driver.find_element_by_css_selector(
        "table.layout:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > button:nth-child(1)").click()
    driver.find_element_by_class_name("Error")
    assert "Пользователя с таким email не существует" in driver.page_source
    driver.quit()


if __name__ == '__main__':
    unittest.main()
