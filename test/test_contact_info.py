from model.contact import Contact
import re


def test_contact_info_on_home_page(app, db):
    contacts = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    len_contacts = len(contacts)
    db_contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
    web_contacts = []
    for i in range(len_contacts):
        web_contacts.append(app.contact.get_contact_info_by_index(i))
    web_contacts_sorted = sorted(web_contacts, key=Contact.id_or_max)
    for i in range(len(web_contacts_sorted)):
        assert clear(web_contacts_sorted[i].firstname) == clear(db_contacts[i].firstname)
        assert clear(web_contacts_sorted[i].lastname) == clear(db_contacts[i].lastname)
        assert clear(web_contacts_sorted[i].address) == clear(db_contacts[i].address)
        assert merge_contact_email_on_edit_page(db_contacts[i]) == clear(web_contacts_sorted[i].all_emails_from_home_page)
        assert merge_contact_phones_on_edit_page(db_contacts[i]) == web_contacts_sorted[i].all_phones_from_home_page


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


