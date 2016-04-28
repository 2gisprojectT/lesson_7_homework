import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    """
        Найти cайт с "картошкой" через поисковую систему Яндекс
        - Проверка работоспособности поисковика на поиск страниц с картошкой.
        - Предусловия отсутствуют;
        - - Открыть Яндекс;
        - - Ввести в поисковую строку "Картошка" и запустить поиск;
        - Яндекс должен найти хотя бы один сайт содержащий картошку.
    """
    def test_case(self):
        driver = self.driver
        driver = webdriver.Firefox()
        driver.get("https://www.yandex.ru")
        search = driver.find_element_by_name("text")
        search.send_keys("Картошка")
        search.submit()
        self.assertIn("Картошка", driver.page_source)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
