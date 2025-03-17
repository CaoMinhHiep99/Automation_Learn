*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER_URL}    https://katalon-demo-cura.herokuapp.com/
${BROWSER}    chrome


*** Test Cases ***
Testing_Input_Box
    Set Selenium Implicit Wait    10
    ${title}=    LaunchBrowser    ${BROWSER_URL}    ${BROWSER}
    Log To Console    ${title}
    Click Element    id=btn-make-appointment
    ${username}=    Get Value    xpath=//div[@class="alert alert-info"]//input[@type='text'][@placeholder='Username']
    ${password}=    Get Value    xpath=//div[@class="alert alert-info"]//input[@type='text'][@placeholder='Password']
    Input Text    xpath=//input[@id="txt-username"]    ${username}
    Input Text    xpath=//input[@id="txt-password"]    ${password}
    Click Element    id=btn-login
    Sleep    5
    Page Should Contain    Healthcare Program

*** Keywords ***
LaunchBrowser
    [Arguments]    ${url}    ${appbrower}
    Open Browser    ${url}    ${appbrower}
    Maximize Browser Window
    ${title}=    Get Title
    [Return]    ${title}