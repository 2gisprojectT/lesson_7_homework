from unittest import TestCase
from selenium import webdriver
from selenium import common
from pdb import set_trace2


class TestOneTwoTrip(TestCase):
    """ 
    Предусловия:
	    Заходим на сайт 'https://www.onetwotrip.com/ru/'"
	"""
    def setUp(self):
        driver = webdriver.Firefox()
        driver.get('https://www.onetwotrip.com/ru/')
        driver.implicitly_wait(10)
        self.driver = driver

    """ 
    Проверка на кол-во билетов в наборе:
    Шаги:
        1. Кликаем на кнопку 'Наборный'
        2. Вводим в поле 'Откуда' название любого города на русском, 
        3. Должна появиться еще одна группа полей для набора информации по
        следующему билету, переходим туда.
        4. Делаем 2 и 3 шаг, пока новые группы полей не перестанут появляться.
        5. Подсчитываем кол-во возможных искомых билетов в наборе.
    Ожидаемый рез-ат:
       Это кол-во должно быть равно определенной норме.
    """
    def test_setOrd(self):	
        maxOrd, n, driver = 10, 4, self.driver
        element = driver.find_element_by_css_selector('li.multiway')
        element.click()
        for i in range(0, maxOrd)
            try:
                element = driver.find_element_by_id('from' + str(i))
                element.send_keys('Амстерд')
            except common.exceptions.NoSuchElementException:
                self.assertEqual(self.n, i, "Кол-во возможных искомых билетов в наборе не равно норме")
                break


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
	unittest.main()
