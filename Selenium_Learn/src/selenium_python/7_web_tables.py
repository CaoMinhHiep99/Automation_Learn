from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://cosmocode.io/automation-practice-webtable/')
browser.execute_script("window.scrollTo(0,700)")
table = browser.find_element(By.ID, "countries")
rows = table.find_elements(By.TAG_NAME, "tr")
row_count = len(rows)
print(row_count)
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        if "Vietnam" in cell.text:
            print(f"Found value country: {cell.text}")
            break
        else:
            print(f"Not found expected value: Vietname, just found {cell.text}")