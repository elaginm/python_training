from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
from random import randrange


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_in_group(app):
    old_db_contact = db.get_contact_list()
    contact = Contact(firstname="Nikolay", lastname="Elagin", nickname="Kolja", title="123", company="IT",
                      address="Kazan", homephone="12345678", mobilephone="123456789", email="kolja@nikolay.de",
                      homepage="www.1n2i3k.ru", birthdayday="23", birthdaymonth="January", birthdayyear="1963",
                      address2="No address")
    group = Group(name="New group")
    old_db_group = db.get_group_list()
    if not old_db_group:
        app.group.create(group)
        new_db_group = db.get_group_list()
        gr_id  = new_db_group[0].id
        if not old_db_contact:
            app.contact.create(contact)
            new_db_contact = db.get_contact_list()
            contact_id = new_db_contact[0].id
            app.contact.add_contact_to_group_by_name(contact_id, gr_id)
            pass



    # if not db_contact:
    #     app.contact.create(contact)
    #
    #
    #

    #
    # if db.get_contact_list() == 0:
    #     app.contact.create(contact)
    #     app.contact.delete_first_contact()
    #     new_contacts = db.get_contact_list()
    #     assert len(old_contacts) == len(new_contacts)
    #
    #     app.group.delete_first_group()
    #     new_groups = db.get_group_list()
    #     assert len(old_groups) == len(new_groups)