from model.contact import Contact


def test_edit_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(Firstname="Nikolay", Lastname="Elagin", Nickname="Kolja", Title="123", Company="IT",
                    Address="Kazan", Homephone="12345678", Mobilephone="+7999441111", Email="kolja@nikolay.de",
                    Homepage="www.1n2i3k.ru", BirthdayDay="23", BirthdayMonth="January", BirthdayYear="1963",
                    Address2="No address")
    if app.contact.count() == 0:
        app.contact.create(contact)
        app.contact.edit_first_contact(Contact(Firstname="Mikhail"))
        app.contact.delete_first_contact()
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) == len(new_contacts)
    else:
        contact.id = old_contacts[0].id
        app.contact.edit_first_contact(contact)
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) == len(new_contacts)
        old_contacts[0] = contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_empty_name(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(Firstname="Ivan", Lastname="Taranov")
    if app.contact.count() == 0:
        app.contact.create(Contact(Firstname="", Lastname=""))
        app.contact.edit_first_contact(contact)
        app.contact.delete_first_contact()
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) == len(new_contacts)
    else:
        if app.contact.edit_empty_name():
            app.open_home_page()
        else:
            contact.id = old_contacts[0].id
            app.contact.edit_first_contact(contact)
            new_contacts = app.contact.get_contact_list()
            assert len(old_contacts) == len(new_contacts)
            old_contacts[0] = contact
            assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_edit_non_empty_name(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(Firstname="", Lastname="")
    if app.contact.count() == 0:
        app.contact.create(Contact(Firstname="Users", Lastname="Test"))
        app.contact.edit_first_contact(contact)
        app.contact.delete_first_contact()
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) == len(new_contacts)
    else:
        if app.contact.edit_empty_name():
            contact.id = old_contacts[0].id
            app.contact.edit_first_contact(contact)
            new_contacts = app.contact.get_contact_list()
            assert len(old_contacts) == len(new_contacts)
            old_contacts[0] = contact
            assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)