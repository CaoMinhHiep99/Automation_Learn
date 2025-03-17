*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER_URL}    https://demo.automationtesting.in/Windows.html
${BROWSER}    chrome


*** Test Cases ***
Testing_Input_Box
    Open Browser    ${BROWSER_URL}    ${BROWSER}
    Maximize Browser Window
    ${location}=    Get Location
    Log To Console    The location 1 is: ${location}

    Go To    https://www.selenium.dev/
    ${location}=    Get Location
    Log To Console    The location 2 is: ${location}

    Go Back
    ${location}=    Get Location
    Log To Console    The location 3 is: ${location}