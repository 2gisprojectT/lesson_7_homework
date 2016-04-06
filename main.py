import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://mail.google.com/")
elem = driver.find_element_by_name("Email")
elem.send_keys("doctorvra4@gmail.com")
elem.send_keys(Keys.RETURN)
time.sleep(1)
elem1 = driver.find_element_by_name("Passwd")
elem1.send_keys("123")
elem1.send_keys(Keys.RETURN)
time.sleep(1)
assert "Указан неправильный адрес или пароль" in driver.page_source
print("Тест пройден")
driver.quit()
