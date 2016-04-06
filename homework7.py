from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://mail.google.com/mail/#inbox")
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