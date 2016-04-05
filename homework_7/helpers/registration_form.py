from homework_7.helpers.base_component import BaseComponent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationWindow(BaseComponent):

    selectors = {
        'self': '.auth__popup',
        'e-mail': '.auth__formFieldEmail',
        'password': '.auth__formFieldPassword',
        'checkbox_licensing_agreement': '.auth__formFieldPseudocheckbox',
        'button_registration': '.auth__formSubmitBtn',
        'link_licensing_agreement': 'li.auth__popupSocialItem:nth-child(1)'
            }

    def filling_the_email_field(self, query):
        self.driver.find_element_by_css_selector(self.selectors['e-mail']).send_keys(query)

    def filling_the_password_field(self, query):
        self.driver.find_element_by_css_selector(self.selectors['password']).send_keys(query)

    def filling_the_checkbox(self):
        self.driver.find_element_by_css_selector(self.selectors['checkbox_licensing_agreement']).click()

    def submit(self):
        self.driver.find_element_by_css_selector(self.selectors['button_registration']).click()

    def clicking_on_a_link_license(self):
        text_checkbox = self.driver.find_element_by_css_selector(self.selectors['self'])
        text_checkbox.find_element_by_link_text('пользовательским соглашением').click()

    def result_registration(self):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'auth__popup'), 'Подтверждение e-mail'))

    def activity_button_register(self):
        class_names = str(self.driver.find_element_by_css_selector(self.selectors['button_registration']).get_attribute('class'))
        if class_names.find('_disabled') == -1:
            button_is_not_active = True
        else:
            button_is_not_active = False
        return(button_is_not_active)

    def registration_window_lights_red(self):
        names_class = str(self.driver.find_element_by_css_selector(self.selectors['self']).get_attribute('class'))
        if names_class.find('_error') == -1:
            error = True
        else:
            error = False
        return(error)

    def clicking_on_a_link_vk_registration(self):
        self.driver.find_element_by_css_selector(self.selectors['link_licensing_agreement']).click()
