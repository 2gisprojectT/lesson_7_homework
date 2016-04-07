from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.yandex.ru")
elem1 = driver.find_element_by_name("text")
elem1.send_keys("Картошка")
elem1.send_keys(Keys.RETURN)
elem = driver.find_element_by_link_text("Найти")
elem.click()


