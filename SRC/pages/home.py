from SRC import utils as u
from Locators import locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

################################################## Header ############################################################################################################
    def click_home_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Head_Home'])).click()
    def click_contact_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(
            locators.Locator.locHome['Head_Contact'])).click()
    def click_about_us_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(
            locators.Locator.locHome['Head_About_Us'])).click()
    def click_cart_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Head_Cart'])).click()
    def click_login_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Head_Login'])).click()
    def set_usernsme(self, username):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located((u.By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[1]/input"))).send_keys(username)
    def set_password(self, password):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located((u.By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[2]/input"))).send_keys(password)
    def click_login(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located((u.By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]"))).click()
    def click_logout_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Head_Logout'])).click()
    def click_signup_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Head_Signup'])).click()
    def click_logo_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Head_Logo'])).click()

#######################################################################################################################################################################

################################################################ Slideshow #################################################################################################

    def click_right_arrow_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(
            locators.Locator.locHome['Slide_Right_Arrow'])).click()
    def click_left_arrow_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(
            locators.Locator.locHome['Slide_Left_Arrow'])).click()
    def click_leftslide_indicator(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(
            locators.Locator.locHome['Slide_LeftSlide_indicator'])).click()
    def click_midleslide_indicator(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(
            locators.Locator.locHome['Slide_MidleSlide_indicator'])).click()
    def click_rightslide_indicator(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(
            locators.Locator.locHome['Slide_RightSlide_indicator'])).click()
