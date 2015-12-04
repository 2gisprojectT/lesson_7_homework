from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.support.select import Select

from helpers.pages.Flights.flights_page import FlightsPage
from helpers.pages.ProfileSettings.profile_settings_page import ProfilePage


class TestProfileSettings(TestCase):
    def setUp(self):
        self.user_email = "i1429637@trbvm.com"
        self.user_password = "projectt"
        self.user_first_name = "Anton"
        self.user_country = {u"Сингапур": "SG"}

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.onetwotrip.com")

        self.profile_page = ProfilePage(self.driver)
        self.flights = FlightsPage(self.driver)

        self.flights.spreader.login_in_form_click()
        register_email_field = self.flights.enter.get_login_email_field()
        register_password_field = self.flights.enter.get_login_password_field()

        register_email_field.send_keys(self.user_email)
        register_password_field.send_keys(self.user_password)
        self.flights.enter.get_login_in_btn().click()

        self.flights.spreader.known_user_form_click()
        self.assertEqual(u"Профиль покупателя",
                         self.profile_page.profile.get_page_title())

    def test_input_correct_last_name(self):
        profile_page = self.profile_page

        profile_page.contacts.get_user_last_name_field().send_keys(self.user_first_name)
        profile_page.contacts.get_save_contacts_btn().click()

        self.driver.refresh()

        self.assertEqual(profile_page.contacts.get_user_last_name_value(), self.user_first_name)

    def test_autocomplete_email_field(self):
        profile_page = self.profile_page

        user_email_autocomplete = profile_page.contacts.get_user_email_field().text

        self.assertIn(self.user_email,
                      user_email_autocomplete)

    def test_select_country(self):
        profile_page = self.profile_page

        selected_user_country = Select(profile_page.contacts.get_user_selected_country_field())
        selected_user_country.select_by_value(self.user_country.get(u"Сингапур"))

        self.assertEqual(profile_page.contacts.get_user_selected_country_value(),
                         self.user_country.get(u"Сингапур"))

    def test_go_to_hotels_page(self):
        profile_page = self.profile_page

        profile_page.profile.get_find_hotels_btn().click()
        self.driver.switch_to.window(self.driver.window_handles[1])

        self.assertIn("hotels", str(self.driver.current_url))

    def test_add_empty_passenger_to_address_book(self):
        profile_page = self.profile_page

        profile_page.passengers.get_add_passenger_btn().click()
        profile_page.passengers.get_save_contacts_btn().click()

        self.assertTrue(profile_page.passengers.get_save_contacts_btn().is_displayed())

    def tearDown(self):
        self.driver.quit()
