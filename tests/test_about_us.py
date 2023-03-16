import unittest
from SRC import utils as u
from SRC.pages import HomePage
class TestAboutUsPage(unittest.TestCase):
    def setUp(self):
        try:
            options = u.WebDriver.ChromeOptions()
            options.add_argument("--disable-extensions")
            self.driver = u.WebDriver.Chrome(options=options)
        except AssertionError:
            self.driver.quit()

    def tearDown(self):
        self.driver.quit()

    ###################################### About us tests ###################################################

    def test_home_btn(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        hp = HomePage
        hp.click_about_us_btn(self)
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located((u.By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div/div/button")))
        play_button = self.driver.find_element(u.By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div/div/button")
        play_button.click()
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located((u.By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div/div/div[4]/button[1]")))
        pause_play = self.driver.find_element(u.By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div/div/div[4]/button[1]")

        self.assertTrue(pause_play)

