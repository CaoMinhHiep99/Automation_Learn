*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER_URL}    https://www.browserstack.com/guide/selenium-scroll-tutorial
${BROWSER}    chrome


*** Test Cases ***
Testing_Input_Box
    Open Browser    ${BROWSER_URL}    ${BROWSER}
    Maximize Browser Window
    # # Roll tới vị trí xác định
    # Execute Javascript    window.scrollTo(0,3000)
    # # Roll tới khi thấy được element
    # Scroll Element Into View    xpath=//div[@class="social-share bottom-center"]//a[@title="Share on Facebook"]
    # Roll xuống cuối page
    Execute Javascript    window.scrollTo(0,document.body.scrollHeight)