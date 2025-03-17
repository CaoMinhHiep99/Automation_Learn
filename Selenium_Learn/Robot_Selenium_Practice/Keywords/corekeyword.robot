*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Resource    ../ResourceQA/utils.robot


*** Variables ***
${BROWSER_URL}    https://demoqa.com/
${BROWSER}    chrome


*** Keywords ***
Open_Browser_App_And_Choose_Element
    [Arguments]    ${options_header}
    ${header_item}=    Run Keyword    Get_Value_Index_List    ${options_header}    header_list
    Open Browser    ${BROWSER_URL}    ${BROWSER}
    Maximize Browser Window
    Click Element    xpath=//h5[text()='${header_item}']


Choose_Page_Practice
    [Arguments]    ${options_header}    ${options_menu}
    # Check Element Visible
    ${header_item}=    Run Keyword    Get_Value_Index_List    ${options_header}    header_list
    ${class}=    SeleniumLibrary.Get Element Attribute    xpath=//div[@class='element-group'][${options_header}]/div[contains(@class, 'element-list')]    class
    Run Keyword If    'show' not in '${class}'    Scroll_Customs    //div[@class="header-text"][text()='${header_item}']
    Run Keyword If    'show' not in '${class}'    Click Element    xpath=//div[@class="header-text"][text()='${header_item}']
    # Choose Page Practice
    ${menu_item}=    Run Keyword    Get_Value_Index_List    ${options_menu}    ${header_item}
    Scroll_Customs    //span[@class="text"][text()='${menu_item}']
    Click Element    xpath=//span[@class="text"][text()='${menu_item}']


LoginInput
    [Arguments]    ${username}    ${password}
    Input Text    xpath=//input[@id="j_username"]    ${username}
    Input Text    xpath=//input[@id="j_password"]    ${password}
    Click Element    xpath=//input[@id="SubmitButton"]

LogOut
    Mouse Over    xpath=//div[@class="dashboard-right-menu"]//span[@aria-hidden="true"] [@class="fa fa-bars fa-2x dashboard-right-menu-icon-color"]
    Mouse Over    xpath=//span[text()='Log Out']
    Click Element    xpath=//span[text()='Log Out']

Expected Value
    [Arguments]    ${expected_value}
    Page Should Contain    ${expected_value}

Check And Open Browser
    ${result}=    Run Keyword And Ignore Error    Get Window Handles
    ${windows}=    Set Variable If    '${result[0]}' == 'PASS'    ${result[1]}    []
    Run Keyword If    ${windows} == []    Open_Browser_App_And_Choose_Element    1