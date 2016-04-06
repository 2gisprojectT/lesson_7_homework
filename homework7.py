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
import time

driver = webdriver.Firefox()
driver.get("http://mail.google.com")
elem = driver.find_element_by_class_name("need-help")

elem.send_keys(Keys.RETURN)

time.sleep(1)
radio = driver.find_element_by_css_selector("input[type='radio'][value='3']")
radio.click()
time.sleep(1)

element = driver.find_element_by_css_selector("[name='Email2']")
element.send_keys("This is not Email")
element.send_keys(Keys.RETURN)
time.sleep(1)
assert "Введите действительный адрес электронной почты." in driver.page_source
print("Тест завершен успешно")
driver.quit()