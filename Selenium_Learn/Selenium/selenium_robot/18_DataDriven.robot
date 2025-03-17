*** Settings ***
Library    SeleniumLibrary
Resource    ../selenium_robot/18_KeyWordLogin.robot

Suite Setup         Run Keywords
...                     OpenBrowerApp    AND
...                     Maximize Browser Window    AND
...                     Set Selenium Implicit Wait    10
Suite Teardown      Run Keyword
...                     CloseBrowerApp
Test Setup          Run Keyword
...                     GoToLogin
Test Teardown       Run Keyword
...                     GoToLogOut

*** Variables ***

*** Test Cases ***
Correct Username
    TestLogin    John Doe    ThisIsNotAPassword
    Expected Value    Make Appointment
Login Fail
    [Teardown]    Log To Console    Login Failed
    TestLogin    a    b
    Expected Value    Login failed! Please ensure the username and password are valid.
*** Keywords ***
TestLogin
    [Arguments]    ${username}    ${password}
    InputUsername    ${username}
    InputPass    ${password}
    ClickLoginButton