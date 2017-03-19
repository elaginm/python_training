from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(Firstname="Nikolay", Lastname="Elagin", Nickname="Kolja", Title="123",
                                           Company="IT", Address="Kazan", Homephone="12345678",
                                           Mobilephone="+7999441111", Email="kolja@nikolay.de",
                                           Homepage="www.1n2i3k.ru", BirthdayDay="14", BirthdayMonth="October",
                                           BirthdayYear="1963", Address2="No address"))
    app.session.logout()