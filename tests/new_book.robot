*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
#Test Setup       Reset Database

*** Test Cases ***

New Book Page Should Be Open
    Go To  ${SERVER}
    Click  css=a[href="/new_book"]
    New Books Page Should Be Open

Each Required Field Must Be Filled
    [Template]    Submission Is Blocked When Required Field Is Empty
    author
    title
    year

Submission Should Fail If Year Is Negative
    Go To  ${NEW_BOOK_URL}
    Fill Field  author  John Smith
    Fill Field  title  Paper Title
    Fill Field  publisher  Publisher Name
    Fill Field  address  Address Name
    Fill Field  year   -42
    Click  css=button[type="submit"]
    Submission Should Fail With Message  Vuosi ei voi olla negatiivinen

Submission Should Fail If Year Is In The Future
    Go To  ${NEW_BOOK_URL}
    Fill Field  author  John Smith
    Fill Field  title  Paper Title
    Fill Field  publisher  Publisher Name
    Fill Field  address  Address Name
    Fill Field  year   2027
    Click  css=button[type="submit"]
    Submission Should Fail With Message  Vuosi ei voi olla tulevaisuudessa

Year Uses Numeric Input
    [Template]    Field Should Be Set As A Number Input
    year

*** Keywords ***

Fill Field
    [Arguments]  ${field_name}  ${value}
    Fill Text  css=input[name="${field_name}"]  ${value}

Submission Should Fail With Message
    [Arguments]  ${message}
    Get Text  body  *=  ${message}

Submission Is Blocked When Required Field Is Empty
    [Arguments]    ${empty_field}
    Go To    ${NEW_BOOK_URL}

    IF    $empty_field != 'author'
        Fill Field  author  John Smith
    END
    IF    $empty_field != 'title'
        Fill Field  title  Example Paper
    END
        IF    $empty_field != 'year'
        Fill Field  year  2026
    END
        IF    $empty_field != 'publisher'
        Fill Field  publisher  Publisher Name
    END
        IF    $empty_field != 'address'
        Fill Field  address  Address Name
    END

    Click    css=button[type="submit"]
    Get Url    ==    ${NEW_BOOK_URL}

Field Should Be Set As A Number Input
    [Arguments]    ${field}
    Go To    ${NEW_BOOK_URL}
    Get Attribute    css=input[name="${field}"]    type    ==    number