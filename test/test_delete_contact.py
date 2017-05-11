from model.contact import Contact
import random
import pytest


def test_delete_some_contact(app, db, check_ui):
    with pytest.allure.step('Given a group list'):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="test"))
        old_contacts = db.get_contact_list()
        contact = random.choice(old_contacts)
    with pytest.allure.step('When I delete a contact %s from the list' % contact):
        app.contact.delete_contact_by_id(contact.id)
    with pytest.allure.step('Then the new contact list is equal to the old list without the deleted contact'):
        assert len(old_contacts) - 1 == app.contact.count()
        # Т.к. после удаления контакта через Веб форму, в БД запись не удаляется,
        # добавил удаление соот-ущего контакта из БД по id
        cursor = db.connection.cursor()
        cursor.execute("delete from addressbook where id=" + contact.id + "")
        new_contacts = db.get_contact_list()
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
        if check_ui:
            with pytest.allure.step('Check UI'):
                assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

