from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_in_group(app):
    old_db_contact = db.get_contact_list()
    old_db_group = db.get_group_list()
    contact = Contact(firstname="Nikolay", lastname="Elagin", nickname="Kolja", title="123", company="IT",
                      address="Kazan", homephone="12345678", mobilephone="123456789", email="kolja@nikolay.de",
                      homepage="www.1n2i3k.ru", birthdayday="23", birthdaymonth="January", birthdayyear="1963",
                      address2="No address")
    group = Group(name="New group")
    if old_db_group:
        new_db_group = db.get_group_list()
        random_group = random.choice(new_db_group)
        group_id = random_group.id
        if old_db_contact:
            contacts_not_in_groups = db.get_contacts_not_in_group(random_group)
            random_contact = random.choice(contacts_not_in_groups)
            contact_id = random_contact.id
            app.contact.add_contact_to_group_by_name(contact_id, group_id)
            app.contact.sort_by_group_by_id(group_id)
            web_info = [app.contact.get_contact_info_by_id(contact_id)]
            db_info = db.get_contacts_in_group(Group(id=str(group_id)))
            assert web_info == db_info
        else:
            app.contact.create(contact)
            new_db_contact = db.get_contact_list()
            contact_id = new_db_contact[0].id
            app.contact.add_contact_to_group_by_name(contact_id, group_id)
            app.contact.sort_by_group_by_id(group_id)
            web_info = [app.contact.get_contact_info_by_id(contact_id)]
            db_info = db.get_contacts_in_group(Group(id=str(group_id)))
            assert web_info == db_info
            app.contact.delete_first_contact()
    else:
        app.group.create(group)
        new_db_group = db.get_group_list()
        group_id = new_db_group[0].id
        if old_db_contact:
            random_contact = random.choice(old_db_contact)
            contact_id = random_contact.id
            app.contact.add_contact_to_group_by_name(contact_id, group_id)
            app.contact.sort_by_group_by_id(group_id)
            web_info = [app.contact.get_contact_info_by_id(contact_id)]
            db_info = db.get_contacts_in_group(Group(id=str(group_id)))
            assert web_info == db_info
        else:
            app.contact.create(contact)
            new_db_contact = db.get_contact_list()
            contact_id = new_db_contact[0].id
            app.contact.add_contact_to_group_by_name(contact_id, group_id)
            app.contact.sort_by_group_by_id(group_id)
            web_info = [app.contact.get_contact_info_by_id(contact_id)]
            db_info = db.get_contacts_in_group(Group(id=str(group_id)))
            assert web_info == db_info
            app.contact.delete_first_contact()
            app.group.delete_first_group()


def test_del_contact_from_group(app):
    db_group = db.get_group_list()
    len_db_group = len(db_group)
    db_contacts = db.get_contact_list()
    contact = Contact(firstname="Nikolay", lastname="Elagin", nickname="Kolja", title="123", company="IT",
                                            address="Kazan", homephone="12345678", mobilephone="123456789", email="kolja@nikolay.de",
                                            homepage="www.1n2i3k.ru", birthdayday="23", birthdaymonth="January", birthdayyear="1963",
                                            address2="No address")
    group = Group(name="New group")
    group_id_list = []
    for i in range(len_db_group):
        group_id_list.append(db_group[i].id)
    if len_db_group:
        if db_contacts:
            for i in range(len_db_group):
                app.contact.select_group_in_filter_by_id(group_id_list[i])
                if db.get_contacts_in_group(db_group[i]):
                    db_contact = db.get_contacts_in_group(db_group[i])
                    random_contact = random.choice(db_contact)
                    random_contact_id = random_contact.id
                    app.contact.delete_contact_from_group(random_contact.id)
                    contacts_not_in_group = db.get_contacts_not_in_group(db_group[i])
                    for i in range (len(contacts_not_in_group)):
                        contact_id_not_in_group = contacts_not_in_group[i].id
                        if random_contact_id == contact_id_not_in_group:
                           print("Контакт id = "+random_contact_id+" успешно удален из группы id = " + group_id_list[i])
        else:
            random_group = random.choice(db_group)
            random_group_id = random_group.id
            app.contact.create(contact)
            new_db_contact = db.get_contact_list()
            contact_id = new_db_contact[0].id
            app.contact.add_contact_to_group_by_name(contact_id, random_group_id)
            contact_in_group = db.get_contacts_in_group(random_group)
            contact_id_in_group = contact_in_group[0].id
            assert contact_id_in_group == contact_id
            app.contact.select_group_in_filter_by_id(random_group_id)
            app.contact.delete_contact_from_group(contact_id)
            contacts_not_in_group = db.get_contacts_not_in_group(random_group)
            contact_id_not_in_group = contacts_not_in_group[0].id
            assert contact_id_not_in_group == contact_id
            app.contact.delete_first_contact()
    else:
        app.group.create(group)
        new_db_group = db.get_group_list()
        group_id = new_db_group[0].id
        if db_contacts:
                    random_contact = random.choice(db_contacts)
                    random_contact_id = random_contact.id
                    app.contact.add_contact_to_group_by_name(random_contact_id, group_id)
                    contact_in_group = db.get_contacts_in_group(new_db_group[0])
                    contact_id_in_group = contact_in_group[0].id
                    assert contact_id_in_group == random_contact_id
                    app.contact.select_group_in_filter_by_id(group_id)
                    app.contact.delete_contact_from_group(random_contact_id)
                    contacts_not_in_group = db.get_contacts_not_in_group(new_db_group[0])
                    contact_id_not_in_group = contacts_not_in_group[0].id
                    assert contact_id_not_in_group == random_contact_id
                    app.group.delete_first_group()
        else:
            app.contact.create(contact)
            new_db_contact = db.get_contact_list()
            contact_id = new_db_contact[0].id
            app.contact.add_contact_to_group_by_name(contact_id, group_id)
            contact_in_group = db.get_contacts_in_group(new_db_group[0])
            contact_id_in_group = contact_in_group[0].id
            assert contact_id_in_group == contact_id
            app.contact.select_group_in_filter_by_id(group_id)
            app.contact.delete_contact_from_group(contact_id)
            contacts_not_in_group = db.get_contacts_not_in_group(new_db_group[0])
            contact_id_not_in_group = contacts_not_in_group[0].id
            assert contact_id_not_in_group == contact_id
            app.contact.delete_first_contact()
            app.group.delete_first_group()