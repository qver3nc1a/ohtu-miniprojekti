*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Database

*** Test Cases ***



*** Keywords ***

Adding Paper Should Succeed
    #TODO

Adding Paper Should Fail With Message
    [Arguments]  ${message}
    Papers Page Should Be Open
    Get Text  body  *=  ${message}