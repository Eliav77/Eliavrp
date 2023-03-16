import unittest
from SRC import utils as u
from SRC.pages import HomePage
class TestCartPage(unittest.TestCase):
    def setUp(self):
        try:
            options = u.WebDriver.ChromeOptions()
            options.add_argument("--disable-extensions")
            self.driver = u.WebDriver.Chrome(options=options)
            self.driver.maximize_window()
            self.driver.get("https://www.demoblaze.com/index.html")
        except AssertionError:
            self.driver.quit()

    def tearDown(self):
        self.driver.quit()


    def test_cart_recovery(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located((u.By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a"))).click()
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located((u.By.XPATH, "/html/body/div[5]/div/div[2]/div[2]/div/a"))).click()
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, "Product added")
        alert.accept()
        hp = HomePage
        hp.click_cart_btn(self)
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located((u.By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr")))
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr").get_attribute("class"), "success")
        self.driver.close()
        options = u.WebDriver.ChromeOptions()
        options.add_argument("--disable-extensions")
        self.driver = u.WebDriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        hp.click_cart_btn(self)
        u.WDW(self.driver, 5)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr").get_attribute("class"), "success")


