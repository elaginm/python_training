# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_adress(Contact(Firstname="Mikhail", Lastname="Elagin", Nickname="MK", Title="Test", Company="Test", Address="qwerty", Homephone="32145678", Mobilephone="324234234",
                         Email="1@2.ru", Homepage="www.234.ru"))
    app.logout()