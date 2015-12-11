from unittest import TestCase

from selenium import webdriver

from helpers.pages.Flights.flights_page import FlightsPage
from helpers.pages.ProfileSettings.profile_settings_page import ProfilePage


class TestProfileSettings(TestCase):
    def setUp(self):
        """
        Prescriptions:
            1.Login in the site with your email and password.
            2.Go to your profile.
        """
        self.user_email = "i1429637@trbvm.com"
        self.user_password = "projectt"
        self.user_first_name = "Anton"
        self.user_country = {u"Сингапур": "SG"}

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.onetwotrip.com")

        self.profile_page = ProfilePage(self.driver)
        self.flights = FlightsPage(self.driver)

        self.flights.spreader.go_to_login_form()
        self.flights.enter.login_in(self.user_email, self.user_password)
        self.flights.spreader.go_to_known_user_form()

        self.assertEqual(u"Профиль покупателя",
                         self.profile_page.profile.get_page_title())

    def test_input_correct_first_name(self):
        """
        Steps:
            1.Input first name in 'First Name' field.
            2.Push the 'Save changes' button.
            3.Refresh the current page.
        """
        profile_page = self.profile_page

        profile_page.contacts.input_first_name(self.user_first_name)

        self.driver.refresh()

        """
        Expected result:
            The entered name was retained in the field.
        """
        self.assertEqual(profile_page.contacts.get_user_first_name_value(),
                         self.user_first_name)

    def test_autocomplete_email_field(self):
        """
        Steps:
            1.Check the 'email' field after autocomplete
        """
        profile_page = self.profile_page

        user_email_autocomplete = profile_page.contacts.get_user_email_text()

        """
        Expected result:
            The email was autocomplete.
        """
        self.assertIn(self.user_email,
                      user_email_autocomplete)

    def test_select_country(self):
        """
        Steps:
            1.Select country in the 'Country' field
            2.Check the 'Country' field
        """
        profile_page = self.profile_page

        profile_page.contacts.select_user_country(self.user_country)

        """
        Expected result:
            The selected country retained in the field.
        """
        self.assertEqual(profile_page.contacts.get_user_selected_country_value(),
                         self.user_country.get(u"Сингапур"))

    def test_go_to_hotels_page(self):
        """
        Steps:
            1.Push the 'Find a hotel' button.
            2.Check transition.
        """
        profile_page = self.profile_page

        profile_page.profile.go_to_hotels_page()
        self.driver.switch_to.window(self.driver.window_handles[1])

        """
        Expected result:
            The transition took place.
        """
        self.assertIn("hotels", str(self.driver.current_url))

    def test_add_empty_passenger_to_address_book(self):
        """
        Steps:
            1.Push the 'Add Passenger' button.
            2.Push the 'Save Changes' button.
            3.Check the 'Save Changes' button status (Displayed).
        """
        profile_page = self.profile_page

        profile_page.passengers.add_passenger()

        """
        Expected result:
            The "Save" button is displayed on the screen.
        """
        self.assertTrue(profile_page.passengers.is_displayed_save_contacts_btn())

    def tearDown(self):
        self.driver.quit()
