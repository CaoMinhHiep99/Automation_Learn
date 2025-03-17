*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER_URL}    https://demo.automationtesting.in/Windows.html
${BROWSER}    chrome


*** Test Cases ***
Testing_Input_Box
    Set Selenium Implicit Wait    10
    Open Browser    ${BROWSER_URL}    ${BROWSER}
    Maximize Browser Window

    Click Button    xpath=//button[@class="btn btn-info"]
    Switch Window    new
    ${title_window}=    Get Title
    Log To Console    ${title_window}
    Sleep    3

    Close All Browsers

    Open Browser    https://demo.automationtesting.in/Windows.html    ${BROWSER}
    Maximize Browser Window

    Open Browser    https://www.selenium.dev/    ${BROWSER}
    Maximize Browser Window

    Switch Browser    2
    ${title_window}=    Get Title
    Log To Console    ${title_window}