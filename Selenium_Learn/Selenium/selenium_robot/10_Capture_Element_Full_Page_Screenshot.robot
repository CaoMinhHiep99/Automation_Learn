*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER_URL}    https://katalon-demo-cura.herokuapp.com/
${BROWSER}    chrome


*** Test Cases ***
Testing_Input_Box
    Set Selenium Implicit Wait    10
    Open Browser    ${BROWSER_URL}    ${BROWSER}
    Maximize Browser Window

    Capture Element Screenshot    //div[@class="text-vertical-center"]    C:/Users/cmhiep/Pictures/Selenium/Test_pic.png
    Capture Page Screenshot    C:/Users/cmhiep/Pictures/Selenium/Test_page_pic.png