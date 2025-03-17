*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER_URL}    https://cosmocode.io/automation-practice-webtable/
${BROWSER}    chrome


*** Test Cases ***
Testing_Input_Box
    Open Browser    ${BROWSER_URL}    ${BROWSER}
    Maximize Browser Window
    ${rows}=    Get Element Count    xpath=//table[@id="countries"]/tbody/tr
    ${cols}=    Get Element Count    xpath=//table[@id="countries"]/tbody/tr[1]/td

    Log To Console    The number of rows: ${rows}
    Log To Console    The number of cols: ${cols}

    ${table_cell}=    Get Text    xpath=//table[@id="countries"]/tbody/tr[194]/td[2]
    Log To Console    ${table_cell}

    Table Column Should Contain    xpath=//table[@id="countries"]    2    Country
    Table Cell Should Contain    xpath=//table[@id="countries"]    194    2    Vietnam
    Table Row Should Contain    xpath=//table[@id="countries"]    194    Vietnam
    # Table Header Should Contain    xpath=//table[@id="countries"]    Visited