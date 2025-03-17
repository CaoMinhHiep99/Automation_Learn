*** Settings ***
Library    RequestsLibrary
Resource    ../RestAPI/API_keyword.robot
Suite Setup        Run Keyword
...                Create Headers And Session

*** Variables ***
${BASE_URL}    https://demoqa.com
${USERNAME}    cmhiep
${PASSWORD}    Hiep1999@
${TOKEN}
${userid}

*** Test Cases ***
Authorized User Check
    [Documentation]    Gửi POST request đến Authorized để kiểm tra đăng nhập
    ${data}    Create Dictionary    userName=${USERNAME}    password=${PASSWORD}
    ${response}=    POST On Session    mysession    ${BASE_URL}/Account/v1/Authorized    json=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be True    ${response.json()}

Create User
    ${data}    Create Dictionary    userName=cmhiep99    password=${PASSWORD}
    ${response}=    POST On Session    mysession    ${BASE_URL}/Account/v1/User    json=${data}
    Should Be Equal As Strings    ${response.status_code}    201
    Should Be True    ${response.json()}
    ${userid}=    Set Variable    ${response.json()['userId']}
    Log To Console    UserID:${userid}

Get Info User
    ${response}=    GET On Session    mysession    ${BASE_URL}/Account/v1/User/6ccbc539-71f2-4468-b3a1-f23a9beef2d4
    Log To Console    ${response.status_code}

*** Keywords ***
Create Headers And Session
    &{headers}=    Create Header
    Create Session    mysession    ${BASE_URL}    headers=${headers}