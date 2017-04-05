# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Mikhail", lastname="Elagin", nickname="MK", title="Test", company="Test",
                      address="qwerty", homephone="32145678", mobilephone="324234234", email="1@2.ru",
                      homepage="www.234.ru", birthdayday="26", birthdaymonth="March", birthdayyear="1985",
                      address2="No address")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", lastname="", nickname="", title="", company="", address="", homephone="",
                      mobilephone="", email="", homepage="", birthdayday="", birthdaymonth="-", birthdayyear="",
                      address2="")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
