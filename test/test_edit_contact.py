from model.contact import Contact
from random import randrange


def test_edit_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(Firstname="Nikolay", Lastname="Elagin", Nickname="Kolja", Title="123", Company="IT",
                      Address="Kazan", Homephone="12345678", Mobilephone="+7999441111", Email="kolja@nikolay.de",
                      Homepage="www.1n2i3k.ru", BirthdayDay="23", BirthdayMonth="January", BirthdayYear="1963",
                      Address2="No address")
    if app.contact.count() == 0:
        app.contact.create(contact)
        app.contact.edit_first_contact(Contact(Firstname="Mikhail"))
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
    contact = Contact(Firstname="Ivan", Lastname="Taranov")
    if app.contact.count() == 0:
        app.contact.create(Contact(Firstname="", Lastname=""))
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
    contact = Contact(Firstname="", Lastname="")
    if app.contact.count() == 0:
        app.contact.create(Contact(Firstname="Users", Lastname="Test"))
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
