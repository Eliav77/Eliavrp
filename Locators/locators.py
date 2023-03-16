import utils as u

class Locator:

    locHome = dict()


    # Header
    locHome['Head_Home'] = (u.By.XPATH, '//a[text()="Home "]')
    locHome['Head_Contact'] = (u.By.XPATH, '//a[text()="Contact"]')
    locHome['Head_About_Us'] = (u.By.XPATH, '//a[text()="About us"]')
    locHome['Head_Cart'] = (u.By.XPATH, '//a[text()="Cart"]')
    locHome['Head_Login'] = (u.By.XPATH, '//a[text()="Log in"]')
    locHome['Head_Logout'] = (u.By.XPATH, '//a[text()="Log out"]')
    locHome['Head_Signup'] = (u.By.XPATH, '//a[text()="Sign up"]')
    locHome['Head_Logo'] = (u.By.XPATH, "/html/body/nav/a")


    # Home
    # Categories
    locHome['Home_Phones'] = (u.By.XPATH, '//a[text()="Phones"]')
    locHome['Home_Laptops'] = (u.By.XPATH, '//a[text()="Laptops"]')
    locHome['Home_Monitors'] = (u.By.XPATH, '//a[text()="Monitors"]')


    # Home
    # Items
    locHome['Items_Collection'] = (u.By.CSS_SELECTOR, '#tbodyid > div')  # item collection

    # Home
    # Navigation buttons
    locHome['NavBtn_Previous'] = (u.By.XPATH, "/html/body/div[5]/div/div[2]/form/ul/li[1]/button")
    locHome['NavBtn_Next'] = (u.By.XPATH, "/html/body/div[5]/div/div[2]/form/ul/li[2]/button")

    # Home
    # Slideshow buttons
    locHome['Slide_Right_Arrow'] = (u.By.XPATH, "/html/body/nav/div[2]/div/a[2]/span[1]")
    locHome['Slide_Left_Arrow'] = (u.By.XPATH, "/html/body/nav/div[2]/div/a[1]/span[1]")
    locHome['Slide_LeftSlide_indicator'] = (u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[1]")
    locHome['Slide_MidleSlide_indicator'] = (u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[2]")
    locHome['Slide_RightSlide_indicator'] = (u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[3]")


    locContact = dict()

    # Contact fields
    locContact['Contact_Email_fld'] = (u.By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[1]/input")
    locContact['Contact_Name_fld'] = (u.By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[2]/input")
    locContact['Message_fld'] = (u.By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[3]/textarea")

    # Contact buttons
    locContact['X_btn'] = (u.By.XPATH, "/html/body/div[1]/div/div/div[1]/button/span")
    locContact['Close_btn'] = (u.By.XPATH, "/html/body/div[1]/div/div/div[3]/button[1]")
    locContact['Send_Message_btn'] = (u.By.XPATH, "/html/body/div[1]/div/div/div[3]/button[2]")



    locProd = dict()

    # Product
    locProd['Product_Add_To_Cart'] = (u.By.XPATH, '//a[text()="Add to cart"]')
    locProd['Product_Undefined_Headline'] = (u.By.XPATH, '//h2[text()="undefined"]')



    # Login and Signup
    locLog = dict()

    locLog['Login_Username'] = (u.By.XPATH, '//*[@id="loginusername"]')
    locLog['Login_Password'] = (u.By.XPATH, '//*[@id="loginpassword"]')
    locLog['Login_Button'] = (u.By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')

    locLog['Signup_Username'] = (u.By.XPATH, '//*[@id="sign-username"]')
    locLog['Signup_Password'] = (u.By.XPATH, '//*[@id="sign-password"]')

    locLog['Signup_Button'] = (u.By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')

    locLog['Welcome'] = (u.By.XPATH, '//*[@id="nameofuser"]')

