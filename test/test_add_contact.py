# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(Firstname="Mikhail", Lastname="Elagin", Nickname="MK", Title="Test", Company="Test",
                      Address="qwerty", Homephone="32145678", Mobilephone="324234234", Email="1@2.ru",
                      Homepage="www.234.ru", BirthdayDay="26", BirthdayMonth="March", BirthdayYear="1985",
                      Address2="No address")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(Firstname="", Lastname="", Nickname="", Title="", Company="", Address="", Homephone="",
                      Mobilephone="", Email="", Homepage="", BirthdayDay="", BirthdayMonth="-", BirthdayYear="",
                      Address2="")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
