from unittest import TestCase
from selenium import webdriver
from selenium import common
from pdb import set_trace


class TestOneTwoTrip(TestCase):
    """ Тест кейс:

    Проверка на кол-во билетов в наборе:
    Предусловия:
        Заходим на сайт 'https://www.onetwotrip.com/ru/'
    Шаги:
        1. Кликаем на кнопку 'Наборный'
        2. Вводим в поле 'Откуда' название любого города на русском
        3. Должна появиться еще одна группа полей для набора информации по
        следующему билету.
        4. Делаем 2 и 3 шаг, пока новые группы полей не перестанут появляться.
        5. Подсчитываем кол-во возможных искомых билетов в наборе.
    Ожидаемый рез-ат:
       Это кол-во должно быть равно норме.

    """

    n = 4

    def setUp(self):
        driver = webdriver.Firefox()
        driver.get('https://www.onetwotrip.com/ru/')
        driver.implicitly_wait(10)
        self.driver = driver

    def test_setOrd(self):
        i, driver = 0, self.driver
        element = driver.find_element_by_css_selector('li.multiway')
        element.click()
        while 1:
            try:
                element = driver.find_element_by_id('from' + str(i))
                element.send_keys('Амстерд')
                i += 1
            except common.exceptions.NoSuchElementException:
                self.assertEqual(self.n, i, "Кол-во возможных искомых билетов в наборе не равно норме")
                break


    def tearDown(self):
        self.driver.quit()


