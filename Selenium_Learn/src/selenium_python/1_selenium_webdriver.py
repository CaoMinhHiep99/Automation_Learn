from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()
username = "standard_user"
password = "secret_sauce"
url = "https://www.saucedemo.com/"
browser.get(url)
# browser.maximize_window()
# browser.set_window_size(800,600)
########################### View ports ####################################
viewports = [(1024, 768), (768,1024), (335, 667), (414, 896), (1920, 1080)]
title = browser.title
for width, height in viewports:
    browser.set_window_size(width, height)
    time.sleep(2)
try:
    if  "Swag Labs" in title:
        user_box_element = browser.find_element(By.ID, "user-name")
        pass_box_element = browser.find_element(By.ID, "password")
        user_box_element.send_keys(username)
        pass_box_element.send_keys(password)
        login_button_element = browser.find_element(By.ID, "login-button")
        login_button_element.click()
        vefify_login = browser.find_element(By.XPATH, "//div[@class='app_logo']")
        if vefify_login.text == "Swag Labs":
            print("Successfully")
        else:
            raise Exception("Login Failed")
        
    else:
        raise Exception("Cannot open the website")
except Exception as ex:
    raise Exception(str(ex))
# browser.back()
# time.sleep(2)
# browser.forward()
# time.sleep(2)
# browser.refresh()
# time.sleep(2)
# browser.close()







# element = browser.find_element(By.XPATH, '//input[@name="username"]')
# element = browser.find_element(By.CLASS_NAME, 'my-class')
# element = browser.find_element(By.CSS_SELECTOR, 'input[name="username"]')
# element = browser.find_element(By.ID, 'username')
# element = browser.find_element(By.LINK_TEXT, 'Click here')
# element = browser.find_element(By.NAME, 'username')
# element = browser.find_element(By.TAG_NAME, 'input')
# element = browser.find_element(By.PARTIAL_LINK_TEXT, 'Click')