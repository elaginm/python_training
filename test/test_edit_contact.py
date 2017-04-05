from model.contact import Contact
from random import randrange


def test_edit_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Nikolay", lastname="Elagin", nickname="Kolja", title="123", company="IT",
                      address="Kazan", homephone="12345678", mobilephone="123456789", email="kolja@nikolay.de",
                      homepage="www.1n2i3k.ru", birthdayday="23", birthdaymonth="January", birthdayyear="1963",
                      address2="No address")
    if app.contact.count() == 0:
        app.contact.create(contact)
        app.contact.edit_first_contact(Contact(firstname="Mikhail"))
        app.contact.delete_first_contact()
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) == len(new_contacts)
    else:
        index = randrange(len(old_contacts))
        contact.id = old_contacts[index].id
        app.contact.edit_contact_by_index(index, contact)
        assert len(old_contacts) == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts[index] = contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_empty_name(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", lastname="Taranov")
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="", lastname=""))
        app.contact.edit_first_contact(contact)
        app.contact.delete_first_contact()
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) == len(new_contacts)
    else:
        index = randrange(len(old_contacts))
        if app.contact.edit_empty_name(index):
            app.open_home_page()
        else:
            contact.id = old_contacts[index].id
            app.contact.edit_contact_by_index(index, contact)
            assert len(old_contacts) == app.contact.count()
            new_contacts = app.contact.get_contact_list()
            old_contacts[index] = contact
            assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_non_empty_name(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", lastname="")
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Users", lastname="Test"))
        app.contact.edit_first_contact(contact)
        app.contact.delete_first_contact()
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) == len(new_contacts)
    else:
        index = randrange(len(old_contacts))
        if app.contact.edit_empty_name(index):
            contact.id = old_contacts[index].id
            app.contact.edit_contact_by_index(index, contact)
            assert len(old_contacts) == app.contact.count()
            new_contacts = app.contact.get_contact_list()
            old_contacts[index] = contact
            assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
