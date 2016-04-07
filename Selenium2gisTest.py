from unittest import TestCase
from selenium import webdriver


class SeleniumTest2GIS(TestCase):
    """Тест Кейс:
        Проверка отображения ссылки на искомый объект в списке результатов поиска
    Предусловия:
        1.Доступ в инетрнет
        2.Перейти на сайте 2gis.ru в firefox
    Шаги:
        1. Ввести в поле поиска адрес/название объекта
        2. Нажать enter
    Ожидаемый результат:
        Ссылка на искомый объект появилась в списке результатов поиска(при условии наличии объекта в базе)
    """

    def setUp(self):

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get("http://2gis.ru/novosibirsk")

    def test_obj_designation(self):

        search_bar = self.driver.find_element_by_class_name("suggest__input")
        search_bar.send_keys("версаль, торгово-офисный центр")
        search_bar.submit()
        self.driver.implicitly_wait(5)
        search_mini_card = self.driver.find_element_by_class_name("miniCard__headerTitleLink")
        search_link = search_mini_card.get_attribute("href")
        self.assertEqual("http://2gis.ru/novosibirsk/firm/141265769436866?queryState=center%2F82.891224%2C54.98376%2Fzoom%2F17", search_link)

    def tearDown(self):
        self.driver.implicitly_wait(30)
        self.driver.quit()
