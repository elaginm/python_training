from random import randrange
import re

def test_contact_info_on_home_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_info_from_home_page = app.contact.get_contact_info_by_index(index)
    contact_info_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_info_from_home_page.firstname == contact_info_from_edit_page.firstname
    assert contact_info_from_home_page.lastname == contact_info_from_edit_page.lastname
    assert contact_info_from_home_page.address == contact_info_from_edit_page.address
    assert contact_info_from_home_page.all_emails_from_home_page == merge_contact_email_on_edit_page(contact_info_from_edit_page)
    assert contact_info_from_home_page.all_phones_from_home_page == merge_contact_phones_on_edit_page(contact_info_from_edit_page)


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


