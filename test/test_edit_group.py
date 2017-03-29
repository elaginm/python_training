from model.group import Group


def test_edit_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name="New group")
    if app.group.count() == 0:
        app.group.create(Group(name="Test group"))
        app.group.edit_first_group(group)
        app.group.delete_first_group()
        new_groups = app.group.get_group_list()
        assert len(old_groups) == len(new_groups)
    else:
        group.id = old_groups[0].id
        app.group.edit_first_group(group)
        assert len(old_groups) == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups[0] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_header(app):
#     old_groups = app.group.get_group_list()
#     group = Group(header="Users")
#     if app.group.count() == 0:
#         app.group.create(Group(header="test"))
#         app.group.edit_first_group(group)
#         app.group.delete_first_group()
#         new_groups = app.group.get_group_list()
#         assert len(old_groups) == len(new_groups)
#     else:
#         app.group.edit_first_group(group)
#         new_groups = app.group.get_group_list()
#         assert len(old_groups) == len(new_groups)


def test_edit_empty_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name="")
    if app.group.count() == 0:
        app.group.create(Group(name="Users"))
        app.group.edit_first_group(group)
        app.group.delete_first_group()
        new_groups = app.group.get_group_list()
        assert len(old_groups) == len(new_groups)
    else:
        if app.group.empty_name():
            app.open_home_page()
        else:
            group.id = old_groups[0].id
            app.group.edit_first_group(group)
            assert len(old_groups) == app.group.count()
            new_groups = app.group.get_group_list()
            old_groups[0] = group
            assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_non_empty_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name="")
    if app.group.count() == 0:
        app.group.create(Group(name="Users"))
        app.group.edit_first_group(group)
        app.group.delete_first_group()
        new_groups = app.group.get_group_list()
        assert len(old_groups) == len(new_groups)
    else:
        if app.group.empty_name():
            group.id = old_groups[0].id
            app.group.edit_first_group(group)
            assert len(old_groups) == app.group.count()
            new_groups = app.group.get_group_list()
            old_groups[0] = group
            assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
