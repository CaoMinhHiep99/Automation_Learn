*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER_URL}    https://demo.automationtesting.in/Static.html
${BROWSER}    chrome


*** Test Cases ***
Testing_Input_Box
    Set Selenium Implicit Wait    10
    Open Browser    ${BROWSER_URL}    ${BROWSER}
    Maximize Browser Window

    Drag And Drop    xpath=//img[@id="angular"]    xpath=//div[@id="droparea"]
    Sleep    3