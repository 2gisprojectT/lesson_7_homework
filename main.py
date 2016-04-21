from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        """Предусловие: зайти на mail.google.com, аутентифицироваться"""
        self.driver = webdriver.Firefox()
        self.driver.get("https://mail.google.com")
        email = self.driver.find_element_by_name("Email")
        email.send_keys("arch.step.inc@gmail.com", Keys.RETURN)
        passw = WW(self.driver, 10).until(EC.presence_of_element_located((By.ID, "Passwd")))
        passw.send_keys("TestinG1234", Keys.RETURN)

    def testWritingLetter(self):
        """
            Название: Успешная отправка сообщения
            Шаги: нажать на кнопку "Написать", в открывшемся окне заполнить данные, нажать кнопку "Отправить"
            Результат: в центре окна появилось сообщение об успешной доставке сообщения
        """

        butt = WW(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "z0"))).click()
        destination = WW(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "to"))).send_keys("arch.step.inc@gmail.com")
        theme = self.driver.find_element_by_name("subjectbox").send_keys("Hello")
        text = self.driver.find_element_by_class_name("LW-avf").send_keys("Hello", Keys.TAB, Keys.ENTER)

        mes = WW(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "vh"),"Письмо отправлено. Просмотреть сообщение"))
        self.assertTrue(mes)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()