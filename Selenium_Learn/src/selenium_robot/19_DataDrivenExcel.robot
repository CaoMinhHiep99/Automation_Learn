*** Settings ***
Library    SeleniumLibrary
Resource    ../selenium_robot/18_KeyWordLogin.robot
Library    DataDriver    ../TestDataCSV/LoginTest.csv    sheet_name=Sheet1

Suite Setup         Run Keywords
...                     OpenBrowerApp    AND
...                     Maximize Browser Window    AND
...                     Set Selenium Implicit Wait    10
Suite Teardown      Run Keyword
...                     CloseBrowerApp

*** Variables ***

*** Test Cases ***
Correct Username
    TestLogin    a    ba    c

*** Keywords ***
TestLogin
    [Arguments]    ${username}    ${password}    ${expected_value}
    InputUsername    ${username}
    InputPass    ${password}
    ClickLoginButton
    Expected Value    ${expected_value}