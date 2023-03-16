import string

from SRC import utils as u
from Locators import locators
import unittest
import SRC.pages.login_sign_up as login_signup


class TestLoginSignUp(unittest.TestCase):
    def setUp(self):
        self.url = 'https://demoblaze.com/index.html'
        self.driver = u.WebDriver.Chrome()
        self.driver.get(self.url)

        self.username = login_signup.rand_string(n=10)
        self.password = login_signup.rand_string(group=string.printable,n=10)

        self.valid_username = "qazwsxedcqaz"
        self.valid_password = "qazwsxedcqaz"


    def test_sign_up(self):
        login_signup.sign_up(self.driver, self.username, self.password)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        try:
            self.assertEqual(alert.text, "Sign up successful.")
            alert.accept()

        except:
            print("The user exists")
            self.assertEqual(alert.text, "This user already exist.")
            alert.accept()


    def test_sign_up_no_values(self):
        login_signup.sign_up(self.driver, "", "")

        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        try:
            self.assertEqual(alert.text, "Please fill out Username and Password.")
            alert.accept()

        except:
            print("Undefined Error")
            alert.accept()


    def test_sign_up_user_only(self):
        """
        test sign up with username only,
        The error I should get is indicator of "Password missing" or something along these lines
        However I don't get those and it returns "Please fill out Username and Password." as alert message.
        :return:
        """
        login_signup.sign_up(self.driver, self.username, "")

        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert


        self.assertEqual(alert.text, "Please fill out Username and Password.")
        alert.accept()


    def test_sign_up_pass_only(self):
        """
        test sign up with password only,
        The error I should get is indicator of "Password missing" or something along these lines
        However I don't get those and it returns "Please fill out Username and Password." as alert message.
        :return:
        """
        login_signup.sign_up(self.driver, "", self.password)

        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        self.assertNotEqual(alert.text, "Please fill out Username and Password.")
        alert.accept()



    def test_login(self):
        login_signup.sign_up(self.driver, self.username, self.password)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        self.driver.switch_to.alert.accept()

        login_signup.login_acc(self.driver, self.username, self.password)

        u.WDW(self.driver, 10).until(u.EC.visibility_of_element_located(locators.Locator.locLog['Welcome']))
        welc_user = self.driver.find_element(u.By.XPATH, '//*[@id="nameofuser"]')

        self.assertEqual(welc_user.text, 'Welcome ' + self.username)


    def test_login_no_values(self):
        login_signup.login_acc(self.driver, "", "")

        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        self.assertEqual(alert.text, "Please fill out Username and Password.")
        alert.accept()



    def test_login_valid_user(self):
        login_signup.login_acc(self.driver, self.valid_username, "")

        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        self.assertNotEqual(alert.text, "Please fill out Username and Password.")
        alert.accept()
        # I would expect the site to tell me I miss only the username



    def test_login_invalid_user(self):
        login_signup.login_acc(self.driver, self.username, "")

        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        self.assertEqual(alert.text, "User does not exist.")
        alert.accept()
        # I would expect the site to tell me the user doesn't exist


    def test_login_invalid_password(self):
        login_signup.login_acc(self.driver, self.valid_username, self.password)

        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        self.assertEqual(alert.text, "Wrong password.")
        alert.accept()
        # I would expect the site to tell me the user doesn't exist


    def test_login_pass_only(self):
        login_signup.login_acc(self.driver, "", self.password)

        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        self.assertNotEqual(alert.text, "Please fill out Username and Password.")
        alert.accept()
        # I would expect the site to tell me I miss only password


    def test_autolog_in_new_tab(self):
        """
        The case is logging into the site and then opening new tab and checking
        wether is connected user is connected or not
        :return:
        """

        login_signup.login_acc(self.driver, self.valid_username, self.valid_password)

        u.open_new_tab(self.driver, self.url)

        u.WDW(self.driver, 10).until(u.EC.visibility_of_element_located(locators.Locator.locLog['Welcome']))
        welc_user = self.driver.find_element(u.By.XPATH, '//*[@id="nameofuser"]')

        self.assertEqual(welc_user.text, 'Welcome ' + self.valid_username)


    def test_autolog_after_quitting_browser(self):
        """
        The case is logging into account and then closing the browser
        The expectation is to be logged in when logging into the site again

        FAILED
        :return:
        """
        login_signup.login_acc(self.driver, self.valid_username, self.valid_password)
        u.sleep(1)

        self.driver.quit()
        u.sleep(2)

        self.driver = u.WebDriver.Chrome()  # re instantiaite driver
        self.driver.get(self.url)

        u.WDW(self.driver, 10).until(u.EC.visibility_of_element_located(locators.Locator.locLog['Welcome']))
        welc_user = self.driver.find_element(u.By.XPATH, '//*[@id="nameofuser"]')

        self.assertEqual(welc_user.text, 'Welcome ' + self.valid_username)


    def test_user_cookie_change(self):
        login_signup.login_acc(self.driver, self.valid_username, self.valid_password)
        u.sleep(1)

        user_data = self.driver.get_cookies()
        self.driver.add_cookie(user_data)
        self.driver.refresh()

        u.WDW(self.driver, 10).until(u.EC.visibility_of_element_located(locators.Locator.locLog['Welcome']))
        welc_user = self.driver.find_element(u.By.XPATH, '//*[@id="nameofuser"]')

        self.assertEqual(welc_user.text, 'Welcome ' + self.valid_username)

    def tearDown(self):
        self.driver.close()