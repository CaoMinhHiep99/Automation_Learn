# *** Settings ***
# Library    RequestsLibrary


# *** Variables ***
# ${BASE_URL}       https://demoqa.com
# ${USERNAME}       cmhiep
# ${PASSWORD}       Hiep1999@
# ${TOKEN}          None

# *** Keywords ***
# Get Token for Authentication
#     [Documentation]    Get lấy Bearer Token
#     Create Session    mysession    ${BASE_URL}
#     ${data}=           Create Dictionary    userName=${USERNAME}    password=${PASSWORD}
#     ${response}=    POST On Session    mysession    ${BASE_URL}/Account/v1/GenerateToken    json=${data}
#     Should Be Equal As Strings    ${response.status_code}    200
#     Log To Console    Token Generated: ${response.json()['token']}
#     ${TOKEN}=    Set Variable    ${response.json()['token']}
#     [Return]    ${TOKEN}

# Create Header
#     ${bearer_token}=    Get Token for Authentication
#     &{headers}=    Create Dictionary    Authorization=${bearer_token}    Content-Type=application/json
#     [Return]    &{headers}

*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}       https://demoqa.com
${USERNAME}       cmhiep
${PASSWORD}       Hiep1999@
${TOKEN}

*** Keywords ***
Get Token for Authentication
    [Documentation]    Get Bearer Token for authentication
    Create Session    mysession    ${BASE_URL}
    ${data}=    Create Dictionary    userName=${USERNAME}    password=${PASSWORD}
    
    # Gửi yêu cầu POST để lấy token
    ${response}=    POST On Session    mysession    /Account/v1/GenerateToken    json=${data}
    Should Be Equal As Numbers    ${response.status_code}    200

    # Chuyển đổi nội dung JSON của response thành dictionary và lấy token
    ${response_json}=    To Json    ${response.text}
    ${TOKEN}=    Set Variable    ${response_json['token']}

    # Log token to console and return token
    Log To Console    Token Generated: ${TOKEN}
    [Return]    JWT ${TOKEN}

Create Header
    [Documentation]    Create header with Bearer token for API requests
    ${Token}=    Get Token for Authentication
    &{headers}=    Create Dictionary    Authorization=${Token}    Content-Type=application/json
    [Return]    &{headers}
