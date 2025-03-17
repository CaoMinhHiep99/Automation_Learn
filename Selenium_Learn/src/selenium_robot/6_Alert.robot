*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER_URL}    https://demo.automationtesting.in/Alerts.html
${BROWSER}    chrome


*** Test Cases ***
Testing_Input_Box
    Set Selenium Implicit Wait    60
    Open Browser    ${BROWSER_URL}    ${BROWSER}
    Maximize Browser Window

    Click Element    xpath=//button[@class="btn btn-danger"]

    Handle Alert    action=accept

    Click Element    xpath=//a[@href="#CancelTab"]

    Click Element    xpath=//button[@class="btn btn-primary"]

    Handle Alert    action=DISMISS

    Click Element    xpath=//button[@class="btn btn-primary"]

    Alert Should Be Present    Press a Button !