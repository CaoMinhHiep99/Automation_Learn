from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://the-internet.herokuapp.com/broken_images')
image_elements = browser.find_elements(By.TAG_NAME, 'img')
broken_images = []
for image in image_elements:
    src = image.get_attribute("src")
    if src:
        response = requests.get(src, verify=False)
        if response.status_code != 200:
            broken_images.append(src)
            print("Broken images found")
if broken_images:
    print("list of broken images:")
    for broken in broken_images:
        print(broken)
else:
    print("No broken images found")