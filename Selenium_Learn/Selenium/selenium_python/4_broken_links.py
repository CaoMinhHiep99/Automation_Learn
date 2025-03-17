from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://jqueryui.com')
link_elements = browser.find_elements(By.TAG_NAME, 'a')
print(f"Total the number of links on the page: {len(link_elements)}")

for link in link_elements:
    href = link.get_attribute('href')
    response = requests.get(href, verify=False)
    if response.status_code >= 400:
        print(f"Broken link: {href} with status code: {response.status_code}")