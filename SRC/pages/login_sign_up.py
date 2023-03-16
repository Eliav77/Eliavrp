import string
import random

from SRC import utils as u
from Locators import locators


def sign_up(driver, username_name = "", password_pass = ""):
    """
    performs signup with details given
    :param driver:
    :param username_name:
    :param password_pass:
    :return:
    """

    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Head_Signup']))
    driver.find_element(u.By.XPATH, '//a[text()="Sign up"]').click()

    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locLog['Signup_Username']))

    signup_username_field = driver.find_element(u.By.XPATH, '//*[@id="sign-username"]')
    signup_username_field.send_keys(username_name)
    print(username_name)

    signup_password_field = driver.find_element(u.By.XPATH, '//*[@id="sign-password"]')
    signup_password_field.send_keys(password_pass)
    print(password_pass)

    signup_btn = driver.find_element(u.By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')
    signup_btn.click()



def login_acc(driver, username="", password=""):
    """
    performs login into existing account
    :param driver:
    :param username:
    :param password:
    :return:
    """

    u.WDW(driver, 20).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Head_Login']))
    driver.find_element(u.By.XPATH, '//a[text()="Log in"]').click()

    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locLog['Login_Username']))

    login_username_field = driver.find_element(u.By.XPATH, '//*[@id="loginusername"]')
    login_username_field.send_keys(username)
    print(username)

    login_password_field = driver.find_element(u.By.XPATH, '//*[@id="loginpassword"]')
    login_password_field.send_keys(password)
    print(password)

    login_btn = driver.find_element(u.By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    login_btn.click()








def rand_string(group = string.ascii_letters, n = 10):
    """
    this function is taking a group of letters and then takes a number.
    it returns a string with random chars from the group in the length of the number  we provided
    :param group:
    :param n:
    :return:
    """
    return ''.join(random.choice(group) for i in range(n))





