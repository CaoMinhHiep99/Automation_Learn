from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

browser = webdriver.Edge()
browser.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
browser.maximize_window()
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
checkbox_index1 = browser.find_element(By.XPATH, "//input[@id='RESULT_CheckBox-8_0']")
browser.execute_script("arguments[0].click();", checkbox_index1)
if checkbox_index1.is_selected():
    browser.execute_script("arguments[0].click();", checkbox_index1)

check_count = 0
try:
    checkbox_all = browser.find_elements(By.XPATH, "//input[@type='checkbox']")
    for checkbox in checkbox_all:
        checkbox.send_keys(Keys.SPACE)
        if checkbox.is_selected():
            check_count +=1
        else:
            print(f"Error: the checkbox at {checkbox} is not selected")
    if check_count != len(checkbox_all):
        raise Exception(
            "Fail to select the checkbox."
            f"Just select {check_count} out of {len(checkbox_all)} checkboxes")
    else:
        print("Successfully to select all the checkboxs")
except Exception as ex:
    raise Exception(str(ex))
