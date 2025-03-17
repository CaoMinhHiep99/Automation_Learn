*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER_URL}    https://katalon-demo-cura.herokuapp.com/
${BROWSER}    chrome

*** Keywords ***
OpenBrowerApp
    Open Browser    ${BROWSER_URL}    ${BROWSER}

CloseBrowerApp
    Close All Browsers

GoToLogin
    Click Element    id=btn-make-appointment

GoToLogOut
    Click Element    xpath=//i[@class="fa fa-bars"]
    Click Element    xpath=//a[@href="authenticate.php?logout"]

InputUsername
    [Arguments]    ${username}
    Input Text    xpath=//input[@id="txt-username"]    ${username}

InputPass
    [Arguments]    ${password}
    Input Text    xpath=//input[@id="txt-password"]    ${password}

ClickLoginButton
    Click Element    id=btn-login

Expected Value
    [Arguments]    ${expected_value}
    Page Should Contain    ${expected_value}