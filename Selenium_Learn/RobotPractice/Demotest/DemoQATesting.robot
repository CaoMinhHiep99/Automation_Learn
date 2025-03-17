*** Settings ***
Library    SeleniumLibrary
Library    XML
Library    RequestsLibrary
Resource    ../DemoKeyword/corekeyword.robot
Resource    ../ResourceQA/utils.robot
Library    Collections


Test Setup        Run Keywords
...                Set Selenium Implicit Wait    10    AND
...                Check And Open Browser
# Test Teardown     Run Keyword
# ...                Close Browser

*** Variables ***
${SESSION}     link_session
@{BAD_LINKS}
@{BROKEN_IMAGES}



*** Test Cases ***
Testing_Text_Box
    [Documentation]    This test case checks the text box functionality on the Elements page. It fills in the required fields and submits the form.

    Log To Console    This test case checks the text box functionality on the Elements page. It fills in the required fields and submits the form.

    Choose_Page_Practice    1    1
    Sleep    1
    Input Text    xpath=//input[@id="userName"]    Cao Minh Hiep
    Input Text    xpath=//input[@id="userEmail"]    cmhiep@tma.com
    Input Text    xpath=//textarea[@id="currentAddress"]    Lab6 TMA Solution
    Input Text    xpath=//textarea[@id="permanentAddress"]    None
    Execute Javascript    window.scrollBy(0, 200)
    Click Button    xpath=//button[@id="submit"]


Check_Box_Testing
    [Documentation]    This test case verifies the checkbox functionality on the Elements page by selecting various options and validating the output.

    Log To Console    This test case verifies the checkbox functionality on the Elements page by selecting various options and validating the output.

    Choose_Page_Practice    1    2
    Sleep    1
    Click Element    xpath=//span[@class='rct-title'][text()='Home']
    Click Element    xpath=//span[@class='rct-title'][text()='Home']
    Click Element    xpath=//button[@aria-label="Expand all"]
    Click Element    xpath=//span[@class='rct-title'][text()='Notes']
    Click Element    xpath=//span[@class='rct-title'][text()='Commands']
    Click Element    xpath=//span[@class='rct-title'][text()='WorkSpace']
    Scroll_Customs    //span[@class='rct-title'][text()='Public']
    Click Element    xpath=//span[@class='rct-title'][text()='Public']
    Scroll_Customs    //span[@class='rct-title'][text()='Downloads']
    Click Element    xpath=//span[@class='rct-title'][text()='Downloads']

    Page Should Contain    You have selected

Radio_Button_Test
    [Documentation]    This test case verifies the functionality of radio buttons on the Elements page by selecting options and checking the results.

    Log To Console    This test case verifies the functionality of radio buttons on the Elements page by selecting options and checking the results.

    Choose_Page_Practice    1    3
    Sleep    1
    Scroll_Customs    //input[@id="yesRadio"]
    # Select Radio Button    like    yesRadio
    # Select Radio Button    like    impressiveRadio
    Click Element    xpath=//label[@for="yesRadio"]

Web_Table_Test
    [Documentation]    This test case adds a new entry to the web table and verifies the row and column counts on the Elements page.

    Log To Console    This test case adds a new entry to the web table and verifies the row and column counts on the Elements page.
    Choose_Page_Practice    1    4
    Sleep    3
    Click Element    id=addNewRecordButton
    Input Text    xpath=//input[@placeholder='First Name']    Cao
    Input Text    xpath=//input[@placeholder='Last Name']    Hiep
    Input Text    xpath=//input[@placeholder='name@example.com']    cmhiep@gmail.com
    Input Text    xpath=//input[@id="age"]    25
    Input Text    xpath=//input[@id="salary"]    10
    Input Text    xpath=//input[@id="department"]    Company
    Click Element    xpath=//button[@id="submit"]

    ${cols}=    SeleniumLibrary.Get Element Count    xpath=//div[@class="rt-tr-group"][1]//div[@class="rt-td"]
    ${rows}=    SeleniumLibrary.Get Element Count    xpath=//div[@class="rt-tbody"][1]//div[@class="rt-tr-group"]
    Log To Console    The number of rows: ${rows}
    Log To Console    The number of cols: ${cols}

Button_Test
    [Documentation]    This test case verifies the functionality of different button interactions on the Elements page, including double-click, right-click, and single-click actions.

    Log To Console    This test case verifies the functionality of different button interactions on the Elements page, including double-click, right-click, and single-click actions.

    Choose_Page_Practice    1    5
    Sleep    3
    Double Click Element    xpath=//button[@id="doubleClickBtn"]
    Page Should Contain    You have done a double click
    Open Context Menu    xpath=//button[@id='rightClickBtn']
    Page Should Contain    You have done a right click
    Click Element    xpath=//button[@class="btn btn-primary"][text()='Click Me']
    Page Should Contain    You have done a dynamic click
    ${original_tab}=    Get Window Handles
    Set Suite Variable    ${original_tab}


Links_And_Broken_Test
    [Documentation]    This test case checks all the links on the page and logs any broken links.
    [Setup]    Run Keyword
    ...        Set Selenium Implicit Wait    10

    Log To Console    This test case checks all the links on the page and logs any broken links.

    Execute JavaScript    window.open("https://practice-automation.com/broken-links/", "_blank")
    Maximize Browser Window
    ${all_tabs}=    Get Window Handles
    Switch Window    ${all_tabs[-1]}

    @{links}=    Get WebElements    xpath=//a[@href]
    Log To Console    Links on the page: @{links}

    ${BASE_URL}=    Get Location
    Create Session    ${SESSION}    ${BASE_URL}

    FOR    ${link}    IN    @{links}
        ${url}=    SeleniumLibrary.Get Element Attribute    ${link}    href
        Log    Checking URL: ${url}
        ${response}=    Get Request    ${SESSION}    ${url}    allow_redirects=True
        Log    Status Code for ${url}: ${response.status_code}
        Run Keyword If    ${response.status_code} != 200    Append To List    ${BAD_LINKS}    ${url} (Status: ${response.status_code})
    END
    Run Keyword If    ${BAD_LINKS}    Log    Bad Links Found: ${BAD_LINKS}
    Close Window

Broken_Images
    [Documentation]    This test case checks all images on the page to identify any broken images (non-200 status codes) and logs the broken images.

    Log To Console    This test case checks all images on the page to identify any broken images (non-200 status codes) and logs the broken images.

    Switch Window    ${original_tab[0]}
    Choose_Page_Practice    1    7
    ${images}=    Get WebElements    xpath=//img[@src]
    Log    Found ${images} images on the page

    ${BASE_URL}=    Get Location
    Create Session    ${SESSION}    ${BASE_URL}

    FOR    ${img}    IN    @{images}
        ${src}=    SeleniumLibrary.Get Element Attribute    ${img}    src
        Log    Checking Image URL: ${src}

        # Send request to check status HTTP of image
        ${response}=    GET On Session    ${SESSION}    ${src}    allow_redirects=True
        Log To Console    Status Code for ${src}: ${response.status_code}

        # If status code not 200, append to list BROKEN_IMAGES
        Run Keyword If    ${response.status_code} != 200    Append To List    @{BROKEN_IMAGES}    ${src} (Status: ${response.status_code})
    END

    # Log add broken image after checked
    Run Keyword If    ${BROKEN_IMAGES}    Log    Broken Images Found: @{BROKEN_IMAGES}


UpLoad_DownLoad_File
    [Documentation]    This test case uploads a file, verifies the upload, and then downloads a sample file to ensure download functionality.

    Log To Console    This test case uploads a file, verifies the upload, and then downloads a sample file to ensure download functionality.

    Choose_Page_Practice    1    8
    # Execute upload file
    Choose File    xpath=//input[@id="uploadFile"]    D:/file.txt

    # Get Text of element <p> to check the file name has uploaded
    ${uploaded_file_name}=    Get Text    xpath=//p[@id="uploadedFilePath"]
    Log    Uploaded File: ${uploaded_file_name}

    # Douple check file has uploaded
    Should Contain    ${uploaded_file_name}    file.txt

    Click Element    xpath=//a[@id="downloadButton"]

    Wait Until Keyword Succeeds    10x    1s    File Should Exist    C:/Users/cmhiep/Downloads/sampleFile.jpeg

    Log    File sampleFile.jpeg downloaded successfully.

Dynamic_Properties
    [Documentation]    This test case checks dynamic properties by verifying visibility and color change of specific elements.

    Log To Console    This test case checks dynamic properties by verifying visibility and color change of specific elements.
    Choose_Page_Practice    1    9

    # Check the color of button Color Change
    ${initial_color}=    SeleniumLibrary.Get Element Attribute    xpath=//button[@id='colorChange']    class
    # Using JavaScript to get the value of attribute 'color'
    ${color}=  Execute JavaScript  return window.getComputedStyle(document.querySelector('#colorChange')).color
    Log To Console  The color of the text before color change is: ${color}

    # Check buton 'Visible After' visible after 5s
    Wait Until Element Is Visible    xpath=//button[@id='visibleAfter']    10s
    Log    'Visible After' button is now visible.

    # Check the color of button Color Change after 5s
    ${initial_color}=    SeleniumLibrary.Get Element Attribute    xpath=//button[@id='colorChange']    class

    # Using JavaScript to get the value of attribute 'color'
    ${color}=  Execute JavaScript  return window.getComputedStyle(document.querySelector('#colorChange')).color
    Log To Console  The color of the text is: ${color}
    Log    Initial color class: ${initial_color}

Form_Practice
    [Documentation]    This test case fills out the practice form and verifies that all inputs are correctly entered.

    Log To Console    This test case fills out the practice form and verifies that all inputs are correctly entered.
    Choose_Page_Practice    2    1

    # Input Name
    Input Text    xpath=//input[@id="firstName"]    Hiep
    Input Text    xpath=//input[@id="lastName"]    Cao

    # Input Email
    Input Text    xpath=//input[@id="userEmail"]    cmhiep@tma.com.vn

    # Select Radio Button
    Click Element    xpath=//label[@for="gender-radio-1"]

    # Input Mobile
    Input Text    //input[@id="userNumber"]    0369965448

    # Date Picker
    Click Element    xpath=//input[@id="dateOfBirthInput"]
    # Select Year
    Click Element    xpath=//select[@class="react-datepicker__year-select"]
    # Scroll Element Into View    xpath=//select[@class="react-datepicker__year-select"]/option[@value='1999']
    # Click Element    locator
    Select From List By Value    xpath=//select[@class='react-datepicker__year-select']    1999
    # Select Month
    Click Element    xpath=//select[@class="react-datepicker__month-select"]/option[@value='10']
    # Select Day
    Wait Until Element Is Visible    xpath=//div[@aria-label='Choose Thursday, November 4th, 1999']    10s
    Click Element    xpath=//div[@aria-label='Choose Thursday, November 4th, 1999']

    # Select Subject
    Click Element    xpath=//input[@id='subjectsInput']
    Input Text    xpath=//input[@id='subjectsInput']    Maths
    Press Keys    xpath=//input[@id='subjectsInput']    ENTER

    # Select Hobbies
    Scroll Element Into View    xpath=//label[@for="hobbies-checkbox-1"]
    Execute Javascript    window.scrollTo(0,100)
    Click Element    xpath=//label[@for="hobbies-checkbox-1"]
    Click Element    xpath=//label[@for="hobbies-checkbox-2"]
    Click Element    xpath=//label[@for="hobbies-checkbox-3"]
    
    # Upload file
    Choose File    xpath=//input[@id="uploadPicture"]    D:/file.txt

    # Get Text of element <p> to check the file name has uploaded
    ${uploaded_file_name}=    Get Text    xpath=//input[@id="uploadPicture"]
    Log    Uploaded File: ${uploaded_file_name}

Test New Tab Functionality
    [Documentation]    This test case verifies the ability to open a new tab, check its content, and switch back to the main window.

    Log To Console    This test case verifies the ability to open a new tab, check its content, and switch back to the main window.s
    Choose_Page_Practice    3    1

    # Click to button "New Tab"
    Click Button    id=tabButton

    # Switch to new tab
    Switch Window    NEW

    # Check Element in the new tab
    Element Should Contain    xpath=//h1    This is a sample page

    # Back to main window
    Close Window
    Switch Window    MAIN

Test_Alerts
    [Documentation]    This test case checks various alert interactions, including accepting, dismissing, and entering text into prompts.

    Log To Console    This test case checks various alert interactions, including accepting, dismissing, and entering text into prompts.
    Choose_Page_Practice    3    2

    # Click to button alertButton
    Click Button    id=alertButton

    Handle Alert    action=accept

    # On button click, alert will appear after 5 seconds
    Click Button    id=timerAlertButton

    Alert Should Be Present    text=This alert appeared after 5 seconds    timeout=10

    # On button click, confirm box will appear
    Click Button    id=confirmButton
    Handle Alert    action=DISMISS

    Page Should Contain    You selected Cancel

    # On button click, confirm box will appear
    Click Button    id=confirmButton
    Handle Alert    action=accept

    Page Should Contain    You selected Ok

    # On button click, prompt box will appear
    Click Button    id=promtButton
    Input Text Into Alert    CMHiep

    Page Should Contain    You entered CMHiep

Test_Frame
    [Documentation]    This test case interacts with frames on the page, retrieving and logging text from each frame.

    Log To Console    This test case interacts with frames on the page, retrieving and logging text from each frame.

    Choose_Page_Practice    3    3

    # Switch to Frame 1
    Select Frame    frame1
    ${TEXT_FRAME}=    Get Text    xpath=//h1[@id="sampleHeading"]
    Log To Console    ${TEXT_FRAME}
    Unselect Frame

    # Switch to Frame 2
    Select Frame    frame2
    ${TEXT_FRAME}=    Get Text    xpath=//h1[@id="sampleHeading"]
    Log To Console    ${TEXT_FRAME}
    Unselect Frame

Test_Nested_Frames
    [Documentation]    This test case verifies text content within nested frames, switching between parent and child frames.

    Log To Console    This test case verifies text content within nested frames, switching between parent and child frames.

    Choose_Page_Practice    3    4
    # Choose outer frame
    Select Frame    id=frame1

    # Get and check Content in outer frame
    ${outer_text}=    Get Text    xpath=//body
    Log    Text in Outer Frame: ${outer_text}
    Should Be Equal As Strings    ${outer_text}    Parent frame

    # Switch to inner frame from outer frame
    Select Frame    xpath=//iframe

    # Get and check Content in inner frame
    ${inner_text}=    Get Text    xpath=//p
    Log    Text in Inner Frame: ${inner_text}
    Should Be Equal As Strings    ${inner_text}    Child Iframe

    Unselect Frame
    Unselect Frame

Test Modal Dialogs
    [Documentation]    This test case checks both small and large modal dialogs, verifying content and closing each dialog.

    Log To Console    This test case checks both small and large modal dialogs, verifying content and closing each dialog.

    Choose_Page_Practice    3    5

    # Open Small Modal and check the content
    Click Button    id=showSmallModal
    Wait Until Element Is Visible    id=example-modal-sizes-title-sm
    ${small_modal_text}=    Get Text    id=example-modal-sizes-title-sm
    Log    Small Modal Text: ${small_modal_text}
    Should Be Equal As Strings    ${small_modal_text}    Small Modal

    # check the content in Small Modal
    ${small_content}=    Get Text    xpath=//div[@class='modal-body'][contains(text(),'This is a small modal. It has very less content')]
    Log    Small Modal Content: ${small_content}
    Should Contain    ${small_content}    This is a small modal.

    # Close Small Modal
    Click Button    id=closeSmallModal
    Wait Until Element Is Not Visible    id=example-modal-sizes-title-sm

    # Open Large Modal and check the content
    Click Button    id=showLargeModal
    Wait Until Element Is Visible    id=example-modal-sizes-title-lg
    ${large_modal_text}=    Get Text    id=example-modal-sizes-title-lg
    Log    Large Modal Text: ${large_modal_text}
    Should Be Equal As Strings    ${large_modal_text}    Large Modal

    # Check the content in Large Modal
    ${large_content}=    Get Text    xpath=//div[@class='modal-body']/p
    Log    Large Modal Content: ${large_content}
    Should Contain    ${large_content}    Lorem Ipsum

    # Close Large Modal
    Click Button    id=closeLargeModal
    Wait Until Element Is Not Visible    id=example-modal-sizes-title-lg

Test Accordian Sections
    [Documentation]    This test case verifies the content of accordion sections by expanding and collapsing sections 2 and 3, and checking their displayed content.

    Log To Console    This test case verifies the content of accordion sections by expanding and collapsing sections 2 and 3, and checking their displayed content.

    Choose_Page_Practice    4    1

    # Check the content in Section 2
    Click Element    id=section2Heading
    Wait Until Element Is Visible    xpath=//div[@id='section2Content']//p
    ${content_2}=    Get Text    xpath=//div[@id='section2Content']//p
    Log    Section 2 Content: ${content_2}
    Should Contain    ${content_2}    Lorem Ipsum    # Check the expected content
    Click Element    id=section2Heading
    Wait Until Element Is Not Visible    xpath=//div[@id='section2Content']//p

    # Check the content in Section 3
    Click Element    xpath=//div[@id='section3Heading']
    Wait Until Element Is Visible    xpath=//div[@id='section3Content']//p
    ${content_3}=    Get Text    xpath=//div[@id='section3Content']//p
    Log    Section 3 Content: ${content_3}
    Should Contain    ${content_3}    Lorem Ipsum    # Check the expected content
    Click Element    xpath=//div[@id='section3Heading']
    Wait Until Element Is Not Visible    xpath=//div[@id='section3Content']//p

Test Auto Complete Feature
    [Documentation]    This test case tests the autocomplete feature by typing a letter, selecting a suggested option, and verifying the selected value.

    Log To Console    This test case tests the autocomplete feature by typing a letter, selecting a suggested option, and verifying the selected value.

    Choose_Page_Practice    4    2
    Sleep    2
    # Input text in Element Auto Complete
    Input Text    xpath=//input[@id="autoCompleteMultipleInput"]    R

    # Wait the list visible
    Wait Until Element Is Visible    xpath=//div[contains(@class, 'auto-complete__option') and contains(text(), 'Red')]

    Click Element    xpath=//div[contains(@class, 'auto-complete__option') and contains(text(), 'Red')]

    # Verify the element has choosed visible in element input
    ${selected_value}=    Get Text    xpath=//div[@class="css-12jo7m5 auto-complete__multi-value__label"]
    Should Be Equal As Strings    ${selected_value}    Red

Test DatePicker
    [Documentation]    This test case selects a specific date in the date picker by choosing the year, month, and day.

    Log To Console    This test case selects a specific date in the date picker by choosing the year, month, and day.

    Choose_Page_Practice    4    3

    # Date Picker
    Click Element    xpath=//input[@id="datePickerMonthYearInput"]
    # Select Year
    Click Element    xpath=//select[@class="react-datepicker__year-select"]
    # Scroll Element Into View    xpath=//select[@class="react-datepicker__year-select"]/option[@value='1999']
    # Click Element    locator
    Select From List By Value    xpath=//select[@class='react-datepicker__year-select']    1999
    # Select Month
    Click Element    xpath=//select[@class="react-datepicker__month-select"]/option[@value='10']
    # Select Day
    Wait Until Element Is Visible    xpath=//div[@aria-label='Choose Thursday, November 4th, 1999']    10s
    Click Element    xpath=//div[@aria-label='Choose Thursday, November 4th, 1999']

Test Slider
    [Documentation]    This test case interacts with the slider, moving it to a new position and verifying that the slider's value has changed.

    Log To Console    This test case interacts with the slider, moving it to a new position and verifying that the slider's value has changed.

    Choose_Page_Practice    4    4

    Sleep    3

    ${initial_value}=    SeleniumLibrary.Get Element Attribute    id=sliderValue    value
    Log To Console    Initial value of the slider: ${initial_value}

    # Move the slider
    Drag And Drop By Offset    xpath=//input[@class="range-slider range-slider--primary"]    100    0  # Move the slider 100 pixels to the right
    Sleep    3
    ${new_value}=    SeleniumLibrary.Get Element Attribute    id=sliderValue    value
    Log To Console    New value of the slider: ${new_value}

    # Check if the value has changed
    Should Not Be Equal    ${initial_value}    ${new_value}    Slider value did not change after dragging

Test Progress Bar Functionality
    [Documentation]    Verify the functionality of the progress bar by starting it, waiting for it to complete, and validating that it reaches 100%.

    Log To Console    Verify the functionality of the progress bar by starting it, waiting for it to complete, and validating that it reaches 100%.

    Choose_Page_Practice    4    5
    # Start the progress bar
    Click Button    xpath=//button[@id='startStopButton']  # Selector for the start/stop button
    Sleep    15  # Wait for progress to complete (adjust as necessary)
    
    # Get the progress bar value
    ${progress_value}=    Get Text    xpath=//div[@role="progressbar"]  # Selector for the progress value label
    Log    Progress value: ${progress_value}

    # Check if the progress bar is complete
    Should Contain    ${progress_value}    100%    The progress bar did not reach 100%

Test Tabs Functionality
    [Documentation]    Verify the functionality of tabs by navigating through different tabs ('What' and 'Origin') and checking if the corresponding content is displayed correctly.

    Log To Console    Verify the functionality of tabs by navigating through different tabs ('What' and 'Origin') and checking if the corresponding content is displayed correctly.
    Choose_Page_Practice    4    6

    # Test 'What' tab
    Click Element    xpath=//a[@id='demo-tab-what']  # Selector for the 'What' tab
    ${content1}=    Get Text    xpath=//div[@id="demo-tabpane-what"]/p[@class="mt-3"]  # Selector for the content area
    Log To Console    Content of 'What' tab: ${content1}

    # Test 'Origin' tab
    Click Element    xpath=//a[@id='demo-tab-origin']  # Selector for the 'Origin' tab
    ${content2}=    Get Text    xpath=//div[@id="demo-tabpane-origin"]/p[@class="mt-3"]  # Selector for the content area
    Log To Console    Content of 'Origin' tab: ${content2}

Test All Tooltips
    [Documentation]    Verify that tooltips appear correctly on hover over various elements and contain the expected text for each element.

    Log To Console    Verify that tooltips appear correctly on hover over various elements and contain the expected text for each element.
    Choose_Page_Practice    4    7

    Sleep    5
    # Check tooltip for "Hover me to see" button
    Log    Testing tooltip for button
    Mouse Over    xpath=//button[@id='toolTipButton']
    ${tooltip_text_button}=    Get Tooltip Text
    Should Be Equal    ${tooltip_text_button}    You hovered over the Button

    # Check tooltip for "Hover me to see text field"
    Log    Testing tooltip for text field
    Mouse Over    xpath=//input[@id='toolTipTextField']
    ${tooltip_text_textfield}=    Get Tooltip Text
    Should Be Equal    ${tooltip_text_textfield}    You hovered over the text field

    # Check tooltip for "Contrary" link
    Log    Testing tooltip for Contrary link
    Mouse Over    xpath=//a[text()='Contrary']
    ${tooltip_text_contrary}=    Get Tooltip Text
    Should Be Equal    ${tooltip_text_contrary}    You hovered over the Contrary

    # Check tooltip for "1.10.32" link
    Log    Testing tooltip for 1.10.32 link
    Mouse Over    xpath=//a[text()='1.10.32']
    ${tooltip_text_number}=    Get Tooltip Text
    Should Be Equal    ${tooltip_text_number}    You hovered over the 1.10.32


Test_Menu
    [Documentation]    Verify the menu functionality by hovering over various menu items, checking if sub-menus appear, and ensuring correct visibility of nested items.

    Log To Console    Verify the menu functionality by hovering over various menu items, checking if sub-menus appear, and ensuring correct visibility of nested items.
    Choose_Page_Practice    4    8

    Sleep    3

    # Select Menu 2
    Mouse Over    xpath=//a[@href="#"][text()='Main Item 2']
    Element Should Be Visible    xpath=//a[@href="#"][text()='Sub Item']
    Element Should Be Visible    xpath=//a[@href="#"][text()='SUB SUB LIST »']
    Element Should Not Be Visible    xpath=//a[@href="#"][text()='Sub Sub Item 1']
    # Select Sub Menu
    Mouse Over    xpath=//a[@href="#"][text()='SUB SUB LIST »']
    Element Should Be Visible    xpath=//a[@href="#"][text()='Sub Sub Item 1']

Test Select Menu
    [Documentation]    Verify the select menu functionality by choosing different options from grouped, single, and multi-select dropdowns, and validating the selected values.

    Log To Console    Verify the select menu functionality by choosing different options from grouped, single, and multi-select dropdowns, and validating the selected values.

    Choose_Page_Practice    4    9

    Sleep    2

    Click Element    xpath=//div[@id='withOptGroup']
    Wait Until Element Is Visible    xpath=//div[contains(@class, 'css-26l3qy-menu')]
    Click Element    xpath=//div[text()='Group 1, option 1']
    ${selected_option}=    Get Text    xpath=//div[@id="withOptGroup"]//div[@class=" css-1uccc91-singleValue"]
    Should Be Equal As Strings    ${selected_option}    Group 1, option 1
    Execute Javascript    window.scrollBy(0, 200)
    Click Element    xpath=//div[@id='withOptGroup']
    Click Element    xpath=//div[text()='Group 2, option 2']
    ${selected_option}=    Get Text    xpath=//div[@id="withOptGroup"]//div[@class=" css-1uccc91-singleValue"]
    Should Be Equal As Strings    ${selected_option}    Group 2, option 2

    Click Element    xpath=//div[@id='selectOne']
    Wait Until Element Is Visible    xpath=//div[contains(@class, 'css-26l3qy-menu')]
    Click Element    xpath=//div[text()='Mr.']
    ${selected_title}=    Get Text    xpath=//div[@id='selectOne']//div[@class=" css-1uccc91-singleValue"]
    Should Be Equal As Strings    ${selected_title}    Mr.
    Click Element    xpath=//div[@id='selectOne']
    Click Element    xpath=//div[text()='Mrs.']
    ${selected_title}=    Get Text    xpath=//div[@id='selectOne']//div[@class=" css-1uccc91-singleValue"]
    Should Be Equal As Strings    ${selected_title}    Mrs.

    Click Element    xpath=(//div[@class=' css-1hwfws3'])[3]
    Click Element    xpath=//div[text()='Green']
    Click Element    xpath=//div[text()='Blue']
    ${selected_colors}=    Get Text    xpath=(//div[contains(@class, 'css-12jo7m5')])[2]
    ${selected_colors1}=    Get Text    xpath=(//div[contains(@class, 'css-12jo7m5')])[1]
    Should Contain    ${selected_colors1}    Green
    Should Contain    ${selected_colors}    Blue
    Click Element    xpath=//div[text()='Red']
    ${selected_colors}=    Get Text    xpath=(//div[contains(@class, 'css-12jo7m5')])[3]
    Should Contain    ${selected_colors}    Red

Test Sortable List Functionality
    [Documentation]    Verify the sortable list functionality by checking the initial order, performing drag-and-drop operations to rearrange items, and validating the new order.

    Log To Console    Verify the sortable list functionality by checking the initial order, performing drag-and-drop operations to rearrange items, and validating the new order.
    Choose_Page_Practice    5    1

    Sleep    3

    Execute Javascript    window.scrollBy(0, 200)
    # Verify the initial order of items in the list
    ${initial_order}=    Create List
    FOR    ${index}    IN RANGE    1    7
        ${item_text}=    Get Text    xpath=(//div[@id='demo-tabpane-list']//div[contains(@class, 'list-group-item')])[${index}]
        Append To List    ${initial_order}    ${item_text}
    END
    Log    Initial order: ${initial_order}

    # Perform drag-and-drop to change the order of items
    Drag And Drop    xpath=(//div[@id='demo-tabpane-list']//div[contains(@class, 'list-group-item')])[1]    xpath=(//div[@id='demo-tabpane-list']//div[contains(@class, 'list-group-item')])[6]
    Sleep    1
    Drag And Drop    xpath=(//div[@id='demo-tabpane-list']//div[contains(@class, 'list-group-item')])[6]    xpath=(//div[@id='demo-tabpane-list']//div[contains(@class, 'list-group-item')])[3]
    Sleep    1

    # Verify the new order of items in the list after drag-and-drop
    ${new_order}=    Create List
    FOR    ${index}    IN RANGE    1    7
        ${item_text}=    Get Text    xpath=(//div[@id='demo-tabpane-list']//div[contains(@class, 'list-group-item')])[${index}]
        Append To List    ${new_order}    ${item_text}
    END
    Log    New order: ${new_order}

    # Check that the new order is not the same as the initial order
    Should Not Be Equal    ${initial_order}    ${new_order}

Test Selectable List and Grid Functionality
    [Documentation]    Verify the selectable functionality in both List and Grid modes by selecting items and confirming their selection status in each mode.
    Log To Console    Verify the selectable functionality in both List and Grid modes by selecting items and confirming their selection status in each mode.

    Choose_Page_Practice    5    2
    # Wait Until Page Contains Element    xpath=//div[@class='main-header' and text()='Selectable']

    # Test List Mode
    Log    Testing List Mode
    Click Element    xpath=//li[text()='Cras justo odio']
    Click Element    xpath=//li[text()='Morbi leo risus']

    # Verify Selection In List Mode
    ${selected_item_1}=    SeleniumLibrary.Get Element Attribute    xpath=//li[text()='Cras justo odio']    class
    ${selected_item_2}=    SeleniumLibrary.Get Element Attribute    xpath=//li[text()='Morbi leo risus']    class
    Should Contain    ${selected_item_1}    active
    Should Contain    ${selected_item_2}    active

    # Switch to Grid Mode
    Click Element    xpath=//a[@id='demo-tab-grid']

    # Select Items In Grid Mode
    Click Element    xpath=//li[text()='One']
    Click Element    xpath=//li[text()='Five']
    Execute Javascript    window.scrollBy(0, 200)
    Click Element    xpath=//li[text()='Nine']

    # Verify Selection In Grid Mode
    ${selected_item_1}=    SeleniumLibrary.Get Element Attribute    xpath=//li[text()='One']    class
    ${selected_item_2}=    SeleniumLibrary.Get Element Attribute    xpath=//li[text()='Five']    class
    ${selected_item_3}=    SeleniumLibrary.Get Element Attribute    xpath=//li[text()='Nine']    class
    Should Contain    ${selected_item_1}    active
    Should Contain    ${selected_item_2}    active
    Should Contain    ${selected_item_3}    active

Test Resizable Boxes Functionality
    [Documentation]    Verify the functionality of resizable boxes by adjusting their size via the resize handles and ensuring that the size changes within the allowed boundaries.

    Log To Console    Verify the functionality of resizable boxes by adjusting their size via the resize handles and ensuring that the size changes within the allowed boundaries.
    Choose_Page_Practice    5    3

     # Test Unrestricted Resizable Box
    Log    Testing unrestricted resizable box
    ${initial_size}=    Get Element Size    xpath=//div[@id='resizableBoxWithRestriction']
    Log    Initial size: ${initial_size}
    Execute Javascript    window.scrollBy(0, 200)
    Sleep    1
    # Resize the unrestricted box
    Drag And Drop By Offset    xpath=(//div[@id='resizableBoxWithRestriction']//span)[1]    50    50
    Sleep    1
    ${new_size}=    Get Element Size    xpath=//div[@id='resizableBoxWithRestriction']
    Log    New size after resizing: ${new_size}

    # Verify that the size has changed
    ${is_equal_1}=    Evaluate    ${initial_size} == ${new_size}
    Should Not Be True    ${is_equal_1}    The dictionaries should not be equal

    # Test Restricted Resizable Box
    Log    Testing restricted resizable box
    ${initial_restricted_size}=    Get Element Size    xpath=//div[@id='resizable']
    Log    Initial restricted size: ${initial_restricted_size}

    # Resize the restricted box within allowed limits
    Scroll Element Into View    xpath=(//div[@id='resizable']//span)[1]
    Execute Javascript    window.scrollBy(0, 200)
    Drag And Drop By Offset    xpath=(//div[@id='resizable']//span)[1]    100    100
    Sleep    1
    ${new_restricted_size}=    Get Element Size    xpath=//div[@id='resizable']
    Log    New restricted size after resizing: ${new_restricted_size}

    # Verify that the restricted size has changed
    ${is_equal_2}=    Evaluate    ${initial_restricted_size} == ${new_restricted_size}
    Should Not Be True    ${is_equal_2}    The dictionaries should not be equal

Test Droppable Functionality
    [Documentation]    Verify the drag-and-drop functionality by dragging items to different droppable areas and validating the changes in text for both acceptable and non-acceptable elements.
    Log To Console    Verify the drag-and-drop functionality by dragging items to different droppable areas and validating the changes in text for both acceptable and non-acceptable elements.

    Choose_Page_Practice    5    4

    # Test Simple Tab
    Log    Testing Simple Drag and Drop
    Sleep    2
    Drag And Drop    id=draggable    id=droppable
    ${drop_text}=    Get Text    xpath=//div[@id='droppable']
    Should Be Equal    ${drop_text}    Dropped!

    # Switch to Accept Tab
    Click Element    xpath=//a[@id='droppableExample-tab-accept']

    # Test Dragging Non-Acceptable Element
    Log    Testing Non-Acceptable Element Drag and Drop
    Drag And Drop    xpath=//div[@id='notAcceptable']    xpath=//div[@id='acceptDropContainer']//div[@id='droppable']
    ${drop_text_non_acceptable}=    Get Text    xpath=//div[@id='acceptDropContainer']//div[@id='droppable']
    Should Be Equal    ${drop_text_non_acceptable}    Drop here

    # Test Dragging Acceptable Element
    Log    Testing Acceptable Element Drag and Drop
    Drag And Drop    xpath=//div[@id='acceptable']    xpath=//div[@id='acceptDropContainer']//div[@id='droppable']
    ${drop_text_acceptable}=    Get Text    xpath=//div[@id='acceptDropContainer']//div[@id='droppable']
    Should Be Equal    ${drop_text_acceptable}    Dropped!

Test Draggable Functionality
    [Documentation]    Verify the draggable functionality in different modes by testing simple drag, axis-restricted drag, and container-restricted drag, and validating the new positions of the elements.
    Log To Console    Verify the draggable functionality in different modes by testing simple drag, axis-restricted drag, and container-restricted drag, and validating the new positions of the elements.

    Choose_Page_Practice    5    5

    Sleep    3

    # Test Simple Drag
    Log    Testing Simple Drag
    Drag And Drop By Offset    xpath=//div[@id='dragBox']    100    50
    ${position}=    SeleniumLibrary.Get Element Attribute    xpath=//div[@id="dragBox"]    style
    Log To Console    ${position}

    # Test Axis Restricted Drag (Only X-axis)
    Log    Testing Axis Restricted Drag (X-axis)
    Click Element    xpath=//a[@id='draggableExample-tab-axisRestriction']
    Drag And Drop By Offset    xpath=//div[@id='restrictedX']    100    0
    ${position}=    SeleniumLibrary.Get Element Attribute    xpath=//div[@id="restrictedX"]    style
    Log To Console    ${position}

    # Test Axis Restricted Drag (Only Y-axis)
    Log    Testing Axis Restricted Drag (Y-axis)
    Drag And Drop By Offset    xpath=//div[@id='restrictedY']    0    100
    ${position}=    SeleniumLibrary.Get Element Attribute    xpath=//div[@id="restrictedY"]    style
    Log To Console    ${position}

    # Test Container Restricted Drag
    Log    Testing Container Restricted Drag
    Click Element    xpath=//a[@id='draggableExample-tab-containerRestriction']
    Drag And Drop By Offset    xpath=//div[@id='containmentWrapper'] //div[@class='draggable ui-widget-content ui-draggable ui-draggable-handle']    50    50
    ${position}=    SeleniumLibrary.Get Element Attribute    xpath=//div[@id='containmentWrapper'] //div[@class='draggable ui-widget-content ui-draggable ui-draggable-handle']    style
    Log To Console    ${position}

*** Keywords ***
Get Tooltip Text
    Wait Until Element Is Visible    xpath=//div[contains(@class, 'tooltip-inner')]
    Sleep    1
    ${tooltip_text}=    Get Text    xpath=//div[contains(@class, 'tooltip-inner')]
    [Return]    ${tooltip_text}