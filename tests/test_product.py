import random
import unittest
from SRC import utils as u
from Locators import locators


class TestProductPage(unittest.TestCase):

    def setUp(self):
        self.url = 'https://demoblaze.com/prod.html?idp_='  # url of the site, idp means the id of the product, should be changed
        # self.service = u.Service()
        self.driver = u.WebDriver.Chrome()
        self.driver.get(self.url)

    def test_product_valid_product(self):
        """
        Test is taking a valid product ID and checks if the page works fine
        after mapping for a while we got 15 products total
        :return:
        """
        for i in range(1, 16):
            new_url = self.url + str(i)
            self.driver.get(new_url)
            u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(
                locators.Locator.locProd['Product_Add_To_Cart']))

            # self.driver.find_element(u.By.XPATH, '//h2[text()="undefined"]').is_displayed()
            self.assertEqual(self.driver.current_url, new_url)
            self.assertFalse(self.driver.find_elements(u.By.XPATH, '//h2[text()="undefined"]'))


    def test_product_invalid_product(self):
        """
        Test is taking invalid ID and checks the result of the page
        We mapped the products IDs and came to a result that the max valid id is 15
        so it means this is the last valid product link
        https://demoblaze.com/prod.html?idp_=15

        p.s this is a negative test
        :return:
        """
        new_url = self.url + str(random.randint(16,9223372036854775807))   # WHY 9223372036854775807? see below
        self.driver.get(new_url)

        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locProd['Product_Add_To_Cart']))

        self.assertTrue(self.driver.find_elements(u.By.XPATH, '//h2[text()="undefined"]'))


    def test_product_insane_product_id(self):
        """
        I wanted to have fun and destroy the url so I did the following
        any product id above 9223372036854775807 or equal to 0 will result in a blank page
        have fun
        technical explanation: apperantly the type of the idp parameters is int. So at first we tried the MAX_INT value 2147483647
        It proceeded so then tested
        p.s this is negative test

        It can be much better to recieve Error 404 or redirection to homepage
        :return:
        """
        new_url = self.url + str(9223372036854775808)
        self.driver.get(new_url)

        u.WDW(self.driver, 3).until(u.EC.invisibility_of_element_located(
            locators.Locator.locProd['Product_Undefined_Headline']), message="This page is blank")

        self.assertFalse(self.driver.find_elements(u.By.XPATH, '//h2[text()="undefined"]'))


    def tearDown(self):
        self.driver.close()