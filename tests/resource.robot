*** Settings ***
Library  Browser

*** Variables ***
${SERVER}     localhost:5001
${DELAY}      500ms
${HOME_URL}   http://${SERVER}
${NEW_PAPER_URL}  http://${SERVER}/new_paper
${NEW_BOOK_URL}  http://${SERVER}/new_book
${PAPERS_URL}  http://${SERVER}/papers
${RESET_URL}  http://${SERVER}/reset_db
${BROWSER}    chromium
${HEADLESS}   false

*** Keywords ***
Open And Configure Browser
    IF  $HEADLESS == 'true'
        New Browser  browser=${BROWSER}  headless=True
    ELSE
        New Browser  browser=${BROWSER}  headless=False  slowMo=${DELAY}
    END
    New Context
    New Page  about:blank

New Papers Page Should Be Open
    Get Title  ==  Uusi artikkeli

New Books Page Should Be Open
    Get Title  ==  Uusi kirja

Reset Database
    Go To  ${RESET_URL}