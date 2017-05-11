from model.contact import Contact
import random
import re
import pytest


def test_edit_contact(app, db, check_ui):
    with pytest.allure.step('Given a non-empty group list'):
        old_contacts = db.get_contact_list()
        contact = Contact(firstname="Nikolay", lastname="Elagin", nickname="Kolja", title="123", company="IT",
                          address="Kazan", homephone="12345678", mobilephone="123456789", email="kolja@nikolay.de",
                          homepage="www.1n2i3k.ru", birthdayday="23", birthdaymonth="January", birthdayyear="1963",
                          address2="No address")
        if app.contact.count() == 0:
            app.contact.create(contact)
            app.contact.edit_first_contact(Contact(firstname="Mikhail"))
            app.contact.delete_first_contact()
            new_contacts = db.get_contact_list()
            assert len(old_contacts) == len(new_contacts)
        else:
            random_contact = random.choice(old_contacts)
            contact.id = random_contact.id
            with pytest.allure.step('When I modify a contact with id=%s in the list' % contact.id):
                app.contact.edit_contact_by_id(random_contact.id, contact)
            with pytest.allure.step('Then the new contact list is equal to the old list with the modified contact'):
                new_contacts = db.get_contact_list()
                assert len(old_contacts) == len(new_contacts)
                result = re.match('^[^:]*', str(random_contact))
                id = result.group(0)
                for i in range(len(old_contacts)):
                    result_old_contacts = re.match('^[^:]*', str(old_contacts[i]))
                    id_old_contacts = result_old_contacts.group(0)
                    if int(id_old_contacts) == int(id):
                        index_contact = i
                old_contacts[index_contact] = contact
                assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
                if check_ui:
                    with pytest.allure.step('check UI'):
                        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                                 key=Contact.id_or_max)


def test_edit_empty_name(app, db, check_ui):
    with pytest.allure.step('Given a non-empty group list'):
        old_contacts = db.get_contact_list()
        contact = Contact(firstname="Ivan", lastname="Taranov")
        if app.contact.count() == 0:
            app.contact.create(Contact(firstname="", lastname=""))
            app.contact.edit_first_contact(contact)
            app.contact.delete_first_contact()
            new_contacts = db.get_contact_list()
            assert len(old_contacts) == len(new_contacts)
        else:
            random_contact = random.choice(old_contacts)
            if app.contact.edit_empty_name_by_id(random_contact.id):
                app.open_home_page()
            else:
                contact.id = random_contact.id
            with pytest.allure.step('When I modify a contact with id=%s in the list' % contact.id):
                app.contact.edit_contact_by_id(random_contact.id, contact)
            with pytest.allure.step('Then the new contact list is equal to the old list with the modified contact'):
                new_contacts = db.get_contact_list()
                assert len(old_contacts) == len(new_contacts)
                result = re.match('^[^:]*', str(random_contact))
                id = result.group(0)
                for i in range(len(old_contacts)):
                    result_old_contacts = re.match('^[^:]*', str(old_contacts[i]))
                    id_old_contacts = result_old_contacts.group(0)
                    if int(id_old_contacts) == int(id):
                        index_contact = i
                old_contacts[index_contact] = contact
                assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
                if check_ui:
                    with pytest.allure.step('check UI'):
                        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                                 key=Contact.id_or_max)


def test_edit_non_empty_name(app, db, check_ui):
    with pytest.allure.step('Given a non-empty group list'):
        old_contacts = db.get_contact_list()
        contact = Contact(firstname="", lastname="")
        if app.contact.count() == 0:
            app.contact.create(Contact(firstname="Users", lastname="Test"))
            app.contact.edit_first_contact(contact)
            app.contact.delete_first_contact()
            new_contacts = db.get_contact_list()
            assert len(old_contacts) == len(new_contacts)
        else:
            random_contact = random.choice(old_contacts)
            if app.contact.edit_empty_name_by_id(random_contact.id):
                contact.id = random_contact.id
            with pytest.allure.step('When I modify a contact with id=%s in the list' % contact.id):
                app.contact.edit_contact_by_id(random_contact.id, contact)
            with pytest.allure.step('Then the new contact list is equal to the old list with the modified contact'):
                new_contacts = db.get_contact_list()
                assert len(old_contacts) == len(new_contacts)
                result = re.match('^[^:]*', str(random_contact))
                id = result.group(0)
                for i in range(len(old_contacts)):
                    result_old_contacts = re.match('^[^:]*', str(old_contacts[i]))
                    id_old_contacts = result_old_contacts.group(0)
                    if int(id_old_contacts) == int(id):
                        index_contact = i
                old_contacts[index_contact] = contact
                assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
                if check_ui:
                    with pytest.allure.step('check UI'):
                        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                                 key=Contact.id_or_max)
