from model.group import Group


# def test_edit_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#         app.group.edit_first_group(Group(name="Users"))
#         app.group.delete_first_group()
#     else:
#         app.group.edit_first_group(Group(name="Users"))
#
#
# def test_edit_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(header="test"))
#         app.group.edit_first_group(Group(header="Users"))
#         app.group.delete_first_group()
#     else:
#         app.group.edit_first_group(Group(header="Users"))
#

def test_edit_empty_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name=""))
        app.group.edit_first_group(Group(name="Users"))
        app.group.delete_first_group()
    else:
        if app.group.empty_name() is not None:
            app.open_home_page()
        else:
            app.group.edit_first_group(Group(name="Usees"))

            #
            # def test_edit_non_empty_name(app):
            #     if app.group.count() == 0:
            #         app.group.create(Group(name="Users"))
            #         app.group.edit_first_group(Group(name=""))
            #         app.group.delete_first_group()
            #     else:
            #         if app.group.empty_name() is not None:
            #             app.group.edit_first_group(Group(name=""))
