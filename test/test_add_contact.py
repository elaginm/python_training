from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*2
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_day():
    return random.randint(1, 31)


def random_string_month():
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
             'August', 'September', 'October', 'November', 'December']
    return random.choice(month)


def random_string_year():
    return random.randint(0, 2030)


testdata = [Contact(firstname="", lastname="", address="", homephone="", mobilephone="", email="",
                    birthdayday="", birthdaymonth="-", birthdayyear="")] + [
            Contact(firstname=random_string("firstname", 10),
                    lastname=random_string("lastname", 10),
                    address=random_string("address", 20),
                    homephone=random_string("", 9),
                    mobilephone=random_string("", 9),
                    email=random_string("email@", 15),
                    birthdayday=str(random_string_day()),
                    birthdaymonth=random_string_month(),
                    birthdayyear=str(random_string_year()))
            for i in range(2)
            ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
#При сравнении списков периодически(т.к. пробелы в тесте рандомны) возникает ошибка, из-за того что в списке
# new_contacts данные берутся с домашней страницы, где в полях сравнения(firstname, lastname)
# двойные пробелы не отображаются. Из-за этого при сравнении списков old и new появлется разница