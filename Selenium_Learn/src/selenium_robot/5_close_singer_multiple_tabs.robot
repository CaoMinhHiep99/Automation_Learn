*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER_URL}    https://katalon-demo-cura.herokuapp.com/
${BROWSER}    chrome


*** Test Cases ***
Testing_Input_Box
    Open Browser    ${BROWSER_URL}    ${BROWSER}
    Maximize Browser Window

    Open Browser    ${BROWSER_URL}    ${BROWSER}
    Maximize Browser Window

    Open Browser    ${BROWSER_URL}    ${BROWSER}
    Maximize Browser Window

    # Close singer browser
    Close Browser

    # Close multiple browser
    Close All Browsers