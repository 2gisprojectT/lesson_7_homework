import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_case(self):
        driver = self.driver

        driver = webdriver.Firefox()
        driver.get("https://www.yandex.ru")
        elem1 = driver.find_element_by_name("text")
        elem1.send_keys("Картошка")
        elem1.send_keys(Keys.RETURN)
        self.assertIn("Картошка", driver.page_source)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


