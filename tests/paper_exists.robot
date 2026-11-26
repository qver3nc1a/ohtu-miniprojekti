*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
#Test Setup       Reset Database

*** Test Cases ***

Paper exists After Submission
    Go To  ${NEW_PAPER_URL}
    Fill Field  key  test
    Fill Field  author  John Smith
    Fill Field  title  Paper Title
    Fill Field  journal  Journal Name
    Fill Field  year   2020
    Fill Field  volume   2
    Fill Field  number   1
    Fill Field  pages   1-4
    Click  css=button[type="submit"]
    Go To  ${PAPERS_URL}
    Get Text  body  *=  John Smith

*** Keywords ***

Fill Field
    [Arguments]  ${field_name}  ${value}
    Fill Text  css=input[name="${field_name}"]  ${value}