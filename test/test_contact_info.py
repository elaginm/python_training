import re


def test_contact_info_on_home_page(app, db):
    contacts = app.contact.get_contact_list()
    len_contacts = len(contacts)
    db_contacts = db.get_contact_list()
    web_contacts = []
    for i in range(len_contacts):
        web_contacts.append(app.contact.get_contact_info_by_index(i))
        assert clear(web_contacts[i].firstname) == clear(db_contacts[i].firstname)
        assert clear(web_contacts[i].lastname) == clear(db_contacts[i].lastname)
        assert clear(web_contacts[i].address) == clear(db_contacts[i].address)
        assert merge_contact_email_on_edit_page(db_contacts[i]) == web_contacts[i].all_emails_from_home_page
        assert merge_contact_phones_on_edit_page(db_contacts[i]) == web_contacts[i].all_phones_from_home_page


def clear(s):
    return re.sub("[() -]", "", s)

def merge_contact_email_on_edit_page(contact):
    return "\n".join(filter(lambda x:  x != "",
              map(lambda x: clear(x),
                  filter(lambda x: x is not None,
                         [contact.email, contact.email2, contact.email3]))))

def merge_contact_phones_on_edit_page(contact):
    return "\n".join(filter(lambda x:  x != "",
              map(lambda x: clear(x),
                  filter(lambda x: x is not None,
                         [contact.homephone, contact.mobilephone,
                          contact.workphone, contact.secondaryphone]))))


