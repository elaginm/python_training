from model.group import Group
from random import randrange


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
        index = randrange(len(old_groups))
        group.id = old_groups[index].id
        app.group.edit_group_by_index(index, group)
        assert len(old_groups) == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups[index] = group
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
    group = Group(name="Test")
    if app.group.count() == 0:
        app.group.create(Group(name=""))
        app.group.edit_first_group(group)
        app.group.delete_first_group()
        new_groups = app.group.get_group_list()
        assert len(old_groups) == len(new_groups)
    else:
        index = randrange(len(old_groups))
        if app.group.empty_name(index):
            app.open_home_page()
        else:
            group.id = old_groups[index].id
            app.group.edit_group_by_index(index, group)
            assert len(old_groups) == app.group.count()
            new_groups = app.group.get_group_list()
            old_groups[index] = group
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
        index = randrange(len(old_groups))
        if app.group.empty_name(index):
            group.id = old_groups[index].id
            app.group.edit_group_by_index(index, group)
            assert len(old_groups) == app.group.count()
            new_groups = app.group.get_group_list()
            old_groups[index] = group
            assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
