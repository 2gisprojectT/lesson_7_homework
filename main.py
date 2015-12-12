# coding: windows-1251
import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistrationForm(TestCase):

    """������������ ����� ����������� ����� "2gis.ru" """


    def setUp(self):

        """
        �������� �������� ����������� � �������� Firefox
        """

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get('http://2gis.ru/novosibirsk/auth/signup')


    def testing_links_to_the_license_agreement(self):

        """
        ������������ ������ "� ���������������� ����������� ����������� � ��������":

        1. ������ �� ������ "� ���������������� ����������� ����������� � ��������".
        """

        """
        �������� �� ������ "� ���������������� ����������� ����������� � ��������"
        """
        text_checkbox = self.driver.find_element_by_class_name('auth__popup')
        link_to_the_license_agreement = text_checkbox.find_element_by_link_text('���������������� �����������')
        link_to_the_license_agreement.click()

        """
        ������������� �� ����������� ����
        """
        names_windows = self.driver.window_handles
        self.driver.switch_to.window(names_windows[1])

        """
        Expected Result
        ��������� ������ ����������������� ���������� � ���� �� ����, ���� � �����.
        """

        """
        ���������, ��� ����������� ���� - ��� ���� � ����������� � ������������ ����������
        """
        self.assertIn("licensing", str(self.driver.current_url))


    def testing_link_authorization_vk(self):

        """
        ������������ ������ �� ����������� ����� "vk.com":

        1. ������ �� ���� � ������� �� vk.com.
        """

        """
        �������� �� ���� � ������� �� vk.com.
        """
        link_vk = self.driver.find_element_by_css_selector('li.auth__popupSocialItem:nth-child(1)')
        link_vk.click()

        """
        Expected Result
        �������� ����� vk.com � ��������� ����� ������� �� ���������� ������� � ��������.
        """

        """
        ��������� � ����������� ���� � ���������, ��� ��� ���� �����������
        """
        names_windows = self.driver.window_handles
        self.driver.switch_to.window(names_windows[1])
        self.assertIn("oauth", str(self.driver.current_url))


    def test_the_password_field(self):

        """
        ������������ ����� ����������� � ������ �������:

        1. ������ � ���� ��� ����������� ����� "test@mail.ru".
        2. �������� ���� ��� ����� ������ ������.
        3. ��������� ������� � �������� "� ���������������� ����������� ����������� � ��������".
        """

        """
        �������� email � ���� '����� ����������� �����'
        """
        email = self.driver.find_element_by_css_selector('.auth__formFieldEmail')
        email.send_keys('test@mail.ru')


        """
         �������� ����������������� ����������
         """
        checkbox = self.driver.find_element_by_class_name('auth__formFieldPseudocheckbox')
        checkbox.click()

        """
        Expected Result
        ������ "������������������" �� ������������, ����������� �� �����������, ������������ �� ������� � ���� ������.
        ��� ������� ������ ������ "������������������" ���������� ��������� �� ������ "�� �� ����� ������!".
        """

        """
        ���������, ��� ������ "������������������" �� �������
        """
        class_names = str(self.driver.find_element_by_css_selector('.auth__formSubmitBtn').get_attribute('class'))
        if class_names.find('_disabled') == -1:
            button_is_not_active = True
        else:
            button_is_not_active = False

        self.assertFalse(button_is_not_active)


    def testing_cooperation_fields_checkbox_is_empty(self):

        """
        ����� ������������ �����. ���� "����������� �����" � "������" ���������� �����, ��� ���, ��� ������� � ���-����� �����������:

        1. ������ � ���� ��� ����������� ����� "test@mail.ru".
        2. ������ � ���� ��� ������ "test123".
        3. ���������, ��� ������� � ���-����� "� ���������������� ���������� ����������� � ��������" �����������.
        4. ������ ������ "������������������".
        """

        """
        �������� ����������� email � ���� '����� ����������� �����'

        """
        email = self.driver.find_element_by_css_selector('.auth__formFieldEmail')
        email.send_keys('test@mail.ru')

        """
         �������� ����������� ������ � ���� '������'
         """
        password = self.driver.find_element_by_css_selector('.auth__formFieldPassword')
        password.send_keys('test123')

        """
         ������� ������ '������������������'
         """
        button_reg = self.driver.find_element_by_class_name('auth__formSubmitBtn')
        button_reg.click()


        """
        Expected Result
        ����������� �� �����������, ������������ �� ������� � ���� ������.
        ��������� �� ������ "�� ������ ������� ������������ ����������".
        """

        """
        ���������, ��� ���� ������������ ������� ������
        """
        class_names = str(self.driver.find_element_by_class_name('auth__popup').get_attribute('class'))
        if class_names.find('_error') == -1:
            error = True
        else:
            error = False
        self.assertFalse(error)


    def testing_cooperation_fields_checkbox_filled(self):
        """
        ����� ������������ �����. ���� "����������� �����" � "������" ���������� �����, ��� ���, ��� ������� � ���-����� ����������:

        1. ������ � ���� "����������� �����" "test@mail.ru"
        2. ������ � ���� ��� ������ "test12345".
        3. ��������� ������� � ����� "� ���������������� ����������� ����������� � ��������".
        4. ������ ������ "������������������".
        """

        """
        �������� ����������� email � ���� '����� ����������� �����'
        """
        self.driver.find_element_by_css_selector('.auth__formFieldEmail').send_keys('test12345@mail.ru')


        """
         �������� ����������� ������ � ���� '������'
         """
        password = self.driver.find_element_by_css_selector('.auth__formFieldPassword')
        password.send_keys('test123')

        """
         �������� ����������������� ����������
        """
        checkbox = self.driver.find_element_by_class_name('auth__formFieldPseudocheckbox')
        checkbox.click()

        """
         ������� ������ '������������������'
        """
        button_reg = self.driver.find_element_by_class_name('auth__formSubmitBtn')
        button_reg.click()

        """
        Expected Result
        ����������� ��������, ������������ ������� � ���� ������. �� email ���������� ������ �� �������� �����������.
        """

        """
        ��������� �������� �� ����������� ���� ���� "������������� e-mail"
        """
        WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'auth__popup'), '������������� e-mail'))


    def tearDown(self):
        """
        �������� �������� ��������
        """

        self.driver.quit()

if __name__ == "__main__":

    unittest.main()