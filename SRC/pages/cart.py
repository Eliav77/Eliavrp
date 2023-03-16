from SRC import utils as u


def add_to_cart_button():
    driver = u.WebDriver.Chrome()
    driver.get("https://demoblaze.com/index.html")
    u.sleep(5)
    driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a').click()
    u.sleep(4)
    add_cart = driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
    add_cart.click()
    u.sleep(4)
    u.WDW(driver, 5).until(u.EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    driver.find_element(u.By.XPATH, '//*[@id="cartur"]').click()
    u.sleep(4)

add_to_cart_button()
