from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


# def test_add_contact_in_group(app):
#     old_db_contact = db.get_contact_list()
#     old_db_group = db.get_group_list()
#     contact = Contact(firstname="Nikolay", lastname="Elagin", nickname="Kolja", title="123", company="IT",
#                       address="Kazan", homephone="12345678", mobilephone="123456789", email="kolja@nikolay.de",
#                       homepage="www.1n2i3k.ru", birthdayday="23", birthdaymonth="January", birthdayyear="1963",
#                       address2="No address")
#     group = Group(name="New group")
#     if old_db_group:
#         new_db_group = db.get_group_list()
#         random_group = random.choice(new_db_group)
#         group_id = random_group.id
#         if old_db_contact:
#             random_contact = random.choice(old_db_contact)
#             contact_id = random_contact.id
#             app.contact.add_contact_to_group_by_name(contact_id, group_id)
#             app.contact.sort_by_group_by_id(group_id)
#             web_info = [app.contact.get_contact_info_by_id(contact_id)]
#             db_info = db.get_contacts_in_group(Group(id=str(group_id)))
#             assert web_info == db_info
#         else:
#             app.contact.create(contact)
#             new_db_contact = db.get_contact_list()
#             contact_id = new_db_contact[0].id
#             app.contact.add_contact_to_group_by_name(contact_id, group_id)
#             app.contact.sort_by_group_by_id(group_id)
#             web_info = [app.contact.get_contact_info_by_id(contact_id)]
#             db_info = db.get_contacts_in_group(Group(id=str(group_id)))
#             assert web_info == db_info
#             # Тест падает на сравении, т.к. в таблице address_in_groups
#             # в столбец deprecated записываются значения '0000-00-00 00:00:00'
#             # для всех контактов, включая те которые в таблице addressbook
#             # в этом поле имеют верное(отличающееся) значение и не отображаются на WEBе
#             app.contact.delete_first_contact()
#     else:
#         app.group.create(group)
#         new_db_group = db.get_group_list()
#         group_id = new_db_group[0].id
#         if old_db_contact:
#             random_contact = random.choice(old_db_contact)
#             contact_id = random_contact.id
#             app.contact.add_contact_to_group_by_name(contact_id, group_id)
#             app.contact.sort_by_group_by_id(group_id)
#             web_info = [app.contact.get_contact_info_by_id(contact_id)]
#             db_info = db.get_contacts_in_group(Group(id=str(group_id)))
#             assert web_info == db_info
#         else:
#             app.contact.create(contact)
#             new_db_contact = db.get_contact_list()
#             contact_id = new_db_contact[0].id
#             app.contact.add_contact_to_group_by_name(contact_id, group_id)
#             app.contact.sort_by_group_by_id(group_id)
#             web_info = [app.contact.get_contact_info_by_id(contact_id)]
#             db_info = db.get_contacts_in_group(Group(id=str(group_id)))
#             assert web_info == db_info
#             app.contact.delete_first_contact()
#             app.group.delete_first_group()


def test_del_contact_from_group(app):
    old_db_group = db.get_group_list()
    len_db_group = len(old_db_group)
    group_id_list = []
    for i in range(len_db_group):
        group_id_list.append(old_db_group[i].id)
    app.contact.find_contact_in_group_and_delete(group_id_list)

    pass
    # +1. Вытащить список get_group_list
    # +2. Из него вытащить все id и добавить в список group_id_list
    # 3. Подставляем idшники из списка в выпадающий список на стр. home
    # 4. Проверяем, есть ли в данной группе контакты и как только находим контакт, удаляем его из группы
    # и проверяем с помощью get_contacts_not_in_group, что контак