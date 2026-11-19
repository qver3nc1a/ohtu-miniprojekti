*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
#Test Setup       Reset Database

*** Test Cases ***

New Paper Page Should Be Open
    Go To  ${NEW_PAPER_URL}
    New Papers Page Should Be Open

Each Required Field Must Be Filled
    [Template]    Submission Is Blocked When Required Field Is Empty
    author
    title
    year

Submission Should Fail If Year Is Negative
    Go To  ${NEW_PAPER_URL}
    Fill Field  author  John Smith
    Fill Field  title  Paper Title
    Fill Field  journal  Journal Name
    Fill Field  year   -42
    Fill Field  volume   2
    Fill Field  number   1
    Fill Field  pages   1-4
    Click  css=button[type="submit"]
    Submission Should Fail With Message  Virheellinen vuosi (täytyy olla 0 < vuosi < 2027)

Submission Should Fail If Year Is In The Future
    Go To  ${NEW_PAPER_URL}
    Fill Field  author  John Smith
    Fill Field  title  Paper Title
    Fill Field  journal  Journal Name
    Fill Field  year   2027
    Fill Field  volume   2
    Fill Field  number   1
    Fill Field  pages   1-4
    Click  css=button[type="submit"]
    Submission Should Fail With Message  Virheellinen vuosi (täytyy olla 0 < vuosi < 2027)

Year Volume And Number Use Numeric Inputs
    [Template]    Field Should Be Set As A Number Input
    year
    volume
    number

*** Keywords ***

Fill Field
    [Arguments]  ${field_name}  ${value}
    Fill Text  css=input[name="${field_name}"]  ${value}

Submission Should Fail With Message
    [Arguments]  ${message}
    Get Text  body  *=  ${message}

Submission Is Blocked When Required Field Is Empty
    [Arguments]    ${empty_field}
    Go To    ${NEW_PAPER_URL}

    IF    $empty_field != 'author'
        Fill Field  author  John Smith
    END
    IF    $empty_field != 'title'
        Fill Field  title  Example Paper
    END
    IF    $empty_field != 'journal'
        Fill Field  journal  Journal Name
    END
        IF    $empty_field != 'year'
        Fill Field  year  2026
    END
        IF    $empty_field != 'volume'
        Fill Field  volume  2
    END
        IF    $empty_field != 'number'
        Fill Field  number  1
    END
        IF    $empty_field != 'pages'
        Fill Field  pages   1-4
    END

    Click    css=button[type="submit"]
    Get Url    ==    ${NEW_PAPER_URL}

Field Should Be Set As A Number Input
    [Arguments]    ${field}
    Go To    ${NEW_PAPER_URL}
    Get Attribute    css=input[name="${field}"]    type    ==    number