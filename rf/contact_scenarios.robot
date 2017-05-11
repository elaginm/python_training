*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures

*** Test Cases ***
Add new contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact  lastname-1  firstname-1  address-1  homephone-1  mobilephone-1  workphone-1  secondaryphone-1  email-1  email2-1  email3-1
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Delete contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${test_contact}=  New Contact  lastname_test  firstname_test  address_test  homephone_test  mobilephone_test  workphone_test  secondaryphone_test  email_test  email2_test  email3_test
    Run Keyword If  ${len}== 0  Create Contact  ${test_contact}
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Edit contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${test_contact}=  New Contact  lastname_test  firstname_test  address_test  homephone_test  mobilephone_test  workphone_test  secondaryphone_test  email_test  email2_test  email3_test
    Run Keyword If  ${len}== 0  Create Contact  ${test_contact}
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${random_contact}=  Get From List  ${old_list}  ${index}
    ${new_data_contact}=  New Contact  lastname_1  firstname_1  address_1  homephone_1  mobilephone_1  workphone_1  secondaryphone_1  email_1  email2_1  email3_1
    Edit Contact  ${random_contact}  ${new_data_contact}
    ${new_list}=  Get Contact List
    Set List Value  ${old_list}  ${index}  ${new_data_contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}
    Run Keyword If  ${len}== 1  Delete First Contact