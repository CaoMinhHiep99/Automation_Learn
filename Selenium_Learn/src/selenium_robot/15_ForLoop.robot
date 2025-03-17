*** Settings ***
Library    SeleniumLibrary

*** Variables ***


*** Test Cases ***
Testing_Input_Box
    FOR    ${counter}    IN RANGE    1    10
        Log To Console    The number is: ${counter}
    END

Loop2
    FOR    ${element}    IN    1  2  3  4  5  6  7  8
        Log To Console    The number is: ${element}
    END

Loop3
    ${list}    Create List    1  2  3  4  5  6  7  8
    FOR    ${element}    IN    @{list}
        Log To Console    The number is: ${element}
    END

Loop4
    ${list}    Create List    1  2  3  4  5  6  7  8
    FOR    ${element}    IN    @{list}
        Log To Console    The number is: ${element}
        Exit For Loop If    ${element}==3
    END