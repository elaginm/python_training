from model.group import Group


def test_edit_name(app):
    app.group.edit_first_group(Group(name="Users"))


def test_edit_header(app):
    app.group.edit_first_group(Group(header="IT"))