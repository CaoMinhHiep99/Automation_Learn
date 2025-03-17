*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
@{header_list}    Elements    Forms    Alerts, Frame & Windows    Widgets    Interactions    Book Store Application
@{Elements_list}    Text Box    Check Box    Radio Button    Web Tables    Buttons    Links    Broken Links - Images    Upload and Download    Dynamic Properties
@{Forms_list}    Practice Form
@{Alerts_Frame_List}    Browser Windows    Alerts    Frames    Nested Frames    Modal Dialogs
@{Widgets_list}    Accordian    Auto Complete    Date Picker    Slider    Progress Bar    Tabs    Tool Tips    Menu    Select Menu
@{Interactions_list}    Sortable    Selectable    Resizable    Droppable    Dragabble
@{Book_Store_list}    Login    Book Store    Profile    Book Store API

*** Keywords ***
Get_List_Based_On_Name
    [Arguments]    ${name}
    @{list}=    Create List
    Run Keyword If    '${name}' == 'header_list'                Set Test Variable    @{list}    @{header_list}
    Run Keyword If    '${name}' == 'Elements'                   Set Test Variable    @{list}    @{Elements_list}
    Run Keyword If    '${name}' == 'Forms'                      Set Test Variable    @{list}    @{Forms_list}
    Run Keyword If    '${name}' == 'Alerts, Frame & Windows'    Set Test Variable    @{list}    @{Alerts_Frame_List}
    Run Keyword If    '${name}' == 'Widgets'                    Set Test Variable    @{list}    @{Widgets_list}
    Run Keyword If    '${name}' == 'Interactions'               Set Test Variable    @{list}    @{Interactions_list}
    Run Keyword If    '${name}' == 'Book Store Application'     Set Test Variable    @{list}    @{Book_Store_list}
    [Return]    @{list}

Get_Value_Index_List
    [Arguments]    ${Number_input}    ${list_name}
    ${index}=    Evaluate    ${Number_input} - 1
    ${expected_list}=    Run Keyword     Get_List_Based_On_Name    ${list_name}
    ${exp_index}=    Set Variable    ${expected_list}[${index}]
    [Return]    ${exp_index}

Scroll_Customs
    [Arguments]    ${locator}
    Scroll Element Into View    xpath=${locator}
    Execute Javascript    window.scrollBy(0, 200)
