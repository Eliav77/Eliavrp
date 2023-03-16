import unittest

from SRC import utils as u
from SRC.pages import HomePage


class TestHomePage(unittest.TestCase):

    def setUp(self):
        try:
            options = u.WebDriver.ChromeOptions()
            options.add_argument("--disable-extensions")
            self.driver = u.WebDriver.Chrome(options=options)
        except AssertionError:
            self.driver.quit()

    def tearDown(self):
        self.driver.quit()

###################################### Home page tests of Header buttons ###################################################
    def test_home_btn(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        hp = HomePage
        hp.click_home_btn(self)
        # assert self.driver.current_url == "https://www.demoblaze.com/index.html"
        self.assertEqual(self.driver.current_url, "https://www.demoblaze.com/index.html")

    def test_contact_btn(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        hp = HomePage
        hp.click_contact_btn(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/div[1]").get_attribute("id"), 'exampleModal')

    def test_about_us_btn(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        hp = HomePage
        hp.click_about_us_btn(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/div[4]").get_attribute("id"), "videoModal")

    def test_cart_btn(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        hp = HomePage
        hp.click_cart_btn(self)
        self.assertEqual(self.driver.current_url, "https://www.demoblaze.com/cart.html")

    def test_login_btn(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        hp = HomePage
        hp.click_login_btn(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/div[3]").get_attribute("id"), "logInModal")

    def test_logout_btn(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        hp = HomePage
        hp.click_login_btn(self)
        hp.set_usernsme(self, "User30")
        hp.set_password(self, "user123")
        hp.click_login(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/nav/div[1]/ul/li[6]/a").get_attribute("text"), "Log out")
        hp.click_logout_btn(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/nav/div[1]/ul/li[5]/a").get_attribute("text"), "Log in")

    def test_signup_btn(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        hp = HomePage
        hp.click_signup_btn(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/div[2]").get_attribute("id"), "signInModal")

    def test_logo_btn(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        hp = HomePage
        hp.click_logo_btn(self)
        self.assertEqual(self.driver.current_url, "https://www.demoblaze.com/index.html")

######################################################################################################################################

######################################## Home page tests of Slideshow buttons #####################################################################

    def test_slideshow_right_arrow(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[1]").get_attribute("class"), "active")
        hp = HomePage
        hp.click_right_arrow_btn(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[2]").get_attribute("class"), "active")

    def test_slideshow_left_arrow(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[1]").get_attribute("class"), "active")
        hp = HomePage
        hp.click_left_arrow_btn(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[3]").get_attribute("class"), "active")

    def test_leftside_indicator(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        hp = HomePage
        hp.click_leftslide_indicator(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[1]").get_attribute("class"), "active")

    def test_midleside_indicator(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        hp = HomePage
        hp.click_midleslide_indicator(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[2]").get_attribute("class"), "active")

    def test_rightside_indicator(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        hp = HomePage
        hp.click_rightslide_indicator(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[3]").get_attribute("class"), "active")