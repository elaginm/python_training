Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <lastname>, <firstname>, <address>, <homephone>, <mobilephone>, <workphone>, <secondaryphone>, <email>, <email2> and <email3>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | lastname  | firstname  | address  | homephone  | mobilephone  | workphone  | secondaryphone  | email  | email2 | email3 |
  | lastname1 | firstname1 | address1 | homephone1 | mobilephone1 | workphone1 | secondaryphone1 | email1 | email2 | email3 |
  | lastname2 | firstname2 | address2 | homephone2 | mobilephone2 | workphone2 | secondaryphone2 | email2 | email2 | email3 |


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact


Scenario: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <lastname>, <firstname>, <address>, <homephone>, <mobilephone>, <workphone>, <secondaryphone>, <email>, <email2> and <email3>
  When I modify the contact in the list
  Then the new contact list is equal to the old list with the modified contact

  Examples:
  | lastname  | firstname  | address  | homephone  | mobilephone  | workphone  | secondaryphone  | email  | email2 | email3 |
  | lastname1 | firstname1 | address1 | homephone1 | mobilephone1 | workphone1 | secondaryphone1 | email1 | email2 | email3 |