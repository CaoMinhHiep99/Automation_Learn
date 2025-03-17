*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER_URL}    https://demoqa.com/frames
${BROWSER}    chrome


*** Test Cases ***
Testing_Input_Box
    Set Selenium Implicit Wait    30
    Open Browser    ${BROWSER_URL}    ${BROWSER}
    Maximize Browser Window

    Select Frame    frame1
    ${TEXT_FRAME}=    Get Text    xpath=//h1[@id="sampleHeading"]
    Log To Console    ${TEXT_FRAME}
    Unselect Frame

    Select Frame    frame2
    ${TEXT_FRAME}=    Get Text    xpath=//h1[@id="sampleHeading"]
    Log To Console    ${TEXT_FRAME}
    Unselect Frame