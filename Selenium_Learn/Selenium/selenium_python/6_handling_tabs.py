from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://www.selenium.dev')
browser.switch_to.new_window()
browser.get('https://playwright.dev/')
number_of_tabs = len(browser.window_handles)
print(f"number_of_tabs: {number_of_tabs}")
tabs_value = browser.window_handles
print(tabs_value)
current_tab = browser.current_window_handle
print(current_tab)
browser.find_element(By.CSS_SELECTOR, ".getStarted_Sjon").click()
FirstTab = browser.window_handles[0]