from unittest import TestCase
from selenium import webdriver


class SeleniumTest2GIS(TestCase):
    def setUp(self):
        """ Предусловие: зайти на сайт 2gis.ru/novosibirsk"""
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get("http://2gis.ru/novosibirsk")

    def test_obj_designation(self):
        """Тест Кейс:
            Проверка отображения ссылки на искомый объект в списке результатов поиска
        Предусловия:
            1.Доступ в инетрнет
            2.Перейти на сайте 2gis.ru в firefox
        Шаги:
            1. Ввести в поле поиска адрес/название объекта
            2. Нажать enter
        Ожидаемый результат:
            Ссылка на искомый объект появилась в списке результатов поиска(при условии наличия объекта в базе)
        """
        search_bar = self.driver.find_element_by_class_name("suggest__input")
        search_bar.send_keys("версаль, торгово-офисный центр")
        search_bar.submit()
        search_list = self.driver.find_element_by_class_name("searchResults__list")
        self.assertIn("Версаль, торгово-офисный центр", search_list.text)

    def tearDown(self):
        """ Завершение сессии """
        self.driver.quit()
