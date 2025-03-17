from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://the-internet.herokuapp.com/broken_images')
iframe = browser.find_elements(By.ID, 'mce_0_ifr')
browser.switch_to.frame(iframe)