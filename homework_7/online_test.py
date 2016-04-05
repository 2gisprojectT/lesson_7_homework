#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from homework_7.helpers.page import Page

information = {
        'e-mail': 'gfhth@mail.ru',
        'password': 'test123'
    }

class SeleniumTest(TestCase):
    """Тестирование формы регистрации сайта "2gis.ru" """

    def setUp(self):
        """
        Открытие страницы регистрации в браузере Firefox
        """

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.page = Page(self.driver)
        self.page.open("http://2gis.ru/novosibirsk/auth/signup")



    def testing_links_to_the_license_agreement(self):
        """
        Тестирование ссылки "С пользовательским соглашением ознакомился и согласен":

        1. Нажать на ссылку "с пользовательским соглашением ознакомился и согласен".
        """
        page = self.page
        driver = self.driver

        page.registration.clicking_on_a_link_license()
        names_windows = self.driver.window_handles
        self.driver.switch_to.window(names_windows[1])

        """
        Expected Result
        Появление текста пользовательского соглашения в этом же окне, либо в новом.
        """
        self.assertIn("licensing", str(self.driver.current_url))

    def testing_link_authorization_vk(self):
        """
        Тестирование ссылки на авторизацию через "vk.com":

        1. Нажать на линк с ссылкой на vk.com.
        """
        page = self.page
        driver = self.driver

        page.registration.clicking_on_a_link_vk_registration()

        """
        Expected Result
        Открытие сайта vk.com и появление формы запроса на разрешение доступа к аккаунту.
        """

        names_windows = self.driver.window_handles
        self.driver.switch_to.window(names_windows[1])
        self.assertIn("oauth", str(self.driver.current_url))

    def test_the_password_field(self):
        """
        Тестирование формы регистрации с пустым паролем:

        1. Ввести в поле для электронной почты "test@mail.ru".
        2. Оставить поле для ввода пароля пустым.
        3. Поставить галочку в чекбоксе "С пользовательским соглашением ознакомился и согласен".
        """
        page = self.page

        page.registration.filling_the_email_field(information['e-mail'])
        page.registration.filling_the_checkbox()

        """
        Expected Result
        Кнопка "Зарегистрироваться" не активирована, регистрация не произведена, пользователь не записан в базу данных.
        При попытке нажать кнопку "Зарегистрироваться" появляется сообщение об ошибке "Вы не ввели пароль!".
        """

        self.assertFalse(page.registration.activity_button_register())

    def testing_cooperation_fields_checkbox_is_empty(self):
        """
        Общее тестирование формы. Поля "Электронный адрес" и "Пароль" заполненны ВЕРНО, при том, что галочка в чек-боксе ОТСУТСТВУЕТ:

        1. Ввести в поле для электронной почты "test@mail.ru".
        2. Ввести в поле для пароля "test123".
        3. Проверить, что галочка в чек-боксе "с пользовательским соглашения ознакомился и согласен" ОТСУТСТВУЕТ.
        4. Нажать кнопку "Зарегистрироваться".
        """
        page = self.page

        page.registration.filling_the_email_field(information['e-mail'])
        page.registration.filling_the_password_field(information['password'])
        page.registration.submit()

        """
        Expected Result
        Регистрация не произведена, пользователь не записан в базу данных.
        Сообщение об ошибке "Вы должны принять лицензионное соглашение".
        """
        self.driver.implicitly_wait(5)
        self.assertFalse(page.registration.registration_window_lights_red())

    def testing_cooperation_fields_checkbox_filled(self):
        """
        Общее тестирование формы. Поля "Электронный адрес" и "Пароль" заполненны ВЕРНО, при том, что галочка в чек-боксе ПОСТАВЛЕНА:

        1. Ввести в поле "Электронная почта" "test@mail.ru"
        2. Ввести в поле для пароля "test12345".
        3. Поставить галочку в боксе "С пользовательским соглашением ознакомился и согласен".
        4. Нажать кнопку "Зарегистрироваться".
        """

        page = self.page

        page.registration.filling_the_email_field(information['e-mail'])
        page.registration.filling_the_password_field(information['password'])
        page.registration.filling_the_checkbox()
        page.registration.submit()

        """
        Expected Result
        Регистрация пройдена, пользователь записан в базу данных. На email отправлено письмо об успешной регистрации.
        """

        page.registration.result_registration()


    def tearDown(self):
        self.page.close()

if __name__ == '__main__':
    unittest.main()