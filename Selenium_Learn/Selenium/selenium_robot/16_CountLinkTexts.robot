*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER_URL}    https://www.browserstack.com/guide/selenium-scroll-tutorial
${BROWSER}    chrome


*** Test Cases ***
Testing_Input_Box
    Open Browser    ${BROWSER_URL}    ${BROWSER}
    # Maximize Browser Window
    ${linkcount}=    Get Element Count    xpath=//a
    Log To Console    ${linkcount}

    FOR    ${i}    IN RANGE    1    ${linkcount}
        ${linktext}=    Get Text    xpath=(//a)[${i}]
        Log To Console    ${linktext}
    END