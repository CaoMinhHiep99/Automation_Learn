*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER_URL}    https://swisnl.github.io/jQuery-contextMenu/demo.html
${BROWSER}    chrome


*** Test Cases ***
Testing_Input_Box
    Set Selenium Implicit Wait    10
    Open Browser    ${BROWSER_URL}    ${BROWSER}
    Maximize Browser Window
    # Right click
    Open Context Menu    xpath=//span[@class="context-menu-one btn btn-neutral"]
    Sleep    3

    Go To    https://testautomationpractice.blogspot.com/
    Maximize Browser Window
    Double Click Element    xpath=//button[@ondblclick="myFunction1()"]
    Sleep    3