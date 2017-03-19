from model.group import Group


def test_edit_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Users"))
    app.session.logout()


def test_edit_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(header="IT"))
    app.session.logout()