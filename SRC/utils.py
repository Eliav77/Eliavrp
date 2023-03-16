import selenium
import requests

from selenium import webdriver as WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service as Service
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

from time import sleep




def open_new_tab(driver, url):

    driver.switch_to.new_window('tab')
    sleep(2)
    driver.get(url)


def close_tab(driver):
    driver.close()
    sleep(2)



