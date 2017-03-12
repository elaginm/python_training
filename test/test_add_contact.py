# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_new_adress(Contact(Firstname="Mikhail", Lastname="Elagin", Nickname="MK", Title="Test", Company="Test", Address="qwerty", Homephone="32145678", Mobilephone="324234234",
                         Email="1@2.ru", Homepage="www.234.ru"))
    app.session.logout()