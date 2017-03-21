from model.contact import Contact


# def test_edit_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(Firstname="Test"))
#         app.contact.edit_first_contact(Contact(Firstname="Mikhail"))
#         app.contact.delete_first_contact()
#     else:
#         app.contact.edit_first_contact(Contact(Firstname="Nikolay", Lastname="Elagin", Nickname="Kolja", Title="123",
#                                            Company="IT", Address="Kazan", Homephone="12345678",
#                                            Mobilephone="+7999441111", Email="kolja@nikolay.de",
#                                            Homepage="www.1n2i3k.ru", BirthdayDay="23", BirthdayMonth="January",
#                                            BirthdayYear="1963", Address2="No address"))

# def test_edit_empty_name(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(Firstname=""))
#         app.contact.edit_first_contact(Contact(Firstname="Ivan"))
#         app.contact.delete_first_contact()
#     else:
#         if app.contact.edit_empty_name() is None:
#             app.contact.edit_first_contact(Contact(Firstname="Nikolay"))



# def test_edit_non_empty_name(app):
#     if app.contact.count() == 0
#         app.contact.create(Contact(Firstname="Users"))
#         app.contact.edit_first_contact(Contact(Firstname=""))
#         app.contact.delete_first_contact()
#     else:
#         if app.contact.empty_name() is not None:
#             app.contact.edit_first_contact(Contact(Firstname=""))