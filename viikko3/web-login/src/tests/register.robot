*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Confirm Password  kalle123
    Submit Registration
    Registration Should Succeed
# ...

Register With Too Short Username And Valid Password
    Set Username  kal
    Set Password  kalle123
    Confirm Password  kalle123
    Submit Registration
    Registration Should Fail With Message  Username must be at least 3 characters long and consist of lowercase letters a-z
# ...

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  kalle12
    Confirm Password  kalle12
    Submit Registration
    Registration Should Fail With Message  Password must be at least 8 characters long
    
# ...

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kalle
    Confirm Password  kalle
    Submit Registration
    Registration Should Fail With Message  Password cannot consist only of letters
# salasana ei sisällä halutunlaisia merkkejä
# ...

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Confirm Password  kalle456
    Submit Registration
    Registration Should Fail With Message  Password and password confirmation do not match
# ...

Register With Username That Is Already In Use
    Create User  existinguser  Valid123!
    Set Username  existinguser
    Set Password  Valid123!
    Confirm Password  Valid123!
    Submit Registration
    Registration Should Fail With Message  Username is already use
#

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm Password 
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Registration Should Succeed
    Main Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}


*** Keywords ***

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Login Page

    

Submit Registration
    Click Button  Register
#...