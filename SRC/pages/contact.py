from SRC import utils as u
from Locators import locators


class ContactModal:

    def __init__(self, driver):
        self.driver = driver

    def set_contact_email(self, email):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(
            locators.Locator.locContact['Contact_Email_fld'])).send_keys(email)
    def set_contact_name(self, name):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(
            locators.Locator.locContact['Contact_Name_fld'])).send_keys(name)
    def set_message(self, message):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(
            locators.Locator.locContact['Message_fld'])).send_keys(message)
    def click_X_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locContact['X_btn'])).click()
    def click_close_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(
            locators.Locator.locContact['Close_btn'])).click()
    def click_send_message_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(
            locators.Locator.locContact['Send_Message_btn'])).click()