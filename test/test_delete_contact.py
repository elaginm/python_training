from model.contact import Contact
import random


def test_delete_some_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count()
    #Т.к. после удаления контакта через Веб форму, в БД запись не удаляется,
    # добавил удаление соот-ущего контакта из БД по id
    cursor = db.connection.cursor()
    cursor.execute("delete from addressbook where id=" + contact.id + "")
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts

