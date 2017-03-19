# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(Firstname="Mikhail", Lastname="Elagin", Nickname="MK", Title="Test", Company="Test",
                               Address="qwerty", Homephone="32145678", Mobilephone="324234234", Email="1@2.ru",
                               Homepage="www.234.ru", BirthdayDay="26", BirthdayMonth="March", BirthdayYear="1985",
                               Address2="No address"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(Firstname="", Lastname="", Nickname="", Title="", Company="", Address="", Homephone="",
                               Mobilephone="", Email="", Homepage="", BirthdayDay="", BirthdayMonth="-",
                               BirthdayYear="", Address2=""))
    app.session.logout()