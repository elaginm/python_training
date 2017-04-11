from model.contact import Contact


def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
#При сравнении списков периодически(т.к. пробелы в тесте рандомны) возникает ошибка, из-за того что в списке
# new_contacts данные берутся с домашней страницы, где в полях сравнения(firstname, lastname)
# двойные пробелы не отображаются. Из-за этого при сравнении списков old и new появлется разница