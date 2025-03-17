*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER_URL}    https://katalon-demo-cura.herokuapp.com/
${BROWSER}    chrome


*** Test Cases ***
Testing_Input_Box
    Open Browser    ${BROWSER_URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains    CURA Healthcare Service    30
    Click Element    id=btn-make-appointment
    ${username}=    Get Value    xpath=//div[@class="alert alert-info"]//input[@type='text'][@placeholder='Username']
    ${password}=    Get Value    xpath=//div[@class="alert alert-info"]//input[@type='text'][@placeholder='Password']
    Input Text    xpath=//input[@id="txt-username"]    ${username}
    Input Text    xpath=//input[@id="txt-password"]    ${password}
    Click Element    id=btn-login
    Sleep    5
    Page Should Contain    Healthcare Program
    Select Radio Button    programs    Medicaid
    Select Checkbox    xpath=//input[@id="chk_hospotal_readmission"]
    Select From List By Index    id=combo_facility    2
    Sleep    1
    Select From List By Label    id=combo_facility    Hongkong CURA Healthcare Center
    Sleep    1
    Select From List By Value    id=combo_facility    Tokyo CURA Healthcare Center