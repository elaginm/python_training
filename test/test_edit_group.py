from model.group import Group
import random


def test_edit_name(app, db, check_ui):
    old_groups = db.get_group_list()
    group = Group(name="New group")
    if app.group.count() == 0:
        app.group.create(Group(name="Test group"))
        app.group.edit_first_group(group)
        app.group.delete_first_group()
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
    else:
        l = len(old_groups)
        random_group_index = random.randrange(l)
        group.id = old_groups[random_group_index].id
        app.group.edit_group_by_id(group.id, group)
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
        old_groups[random_group_index] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
        # random_group = random.choice(old_groups)
        # group.id = random_group.id
        # app.group.edit_group_by_id(group.id, group)
        # new_groups = db.get_group_list()
        # assert len(old_groups) == len(new_groups)
        # result = re.match('^[^:]*', str(random_group))
        # id = result.group(0)
        # index_group = None
        # i = 0
        # while index_group is None and i in range(len(old_groups)):
        #     result_old_group = re.match('^[^:]*', str(old_groups[i]))
        #     id_old_group = result_old_group.group(0)
        #     if (int(id_old_group) == int(id)):
        #         index_group = i
        #     i+=1

def test_edit_empty_name(app, db, check_ui):
    old_groups = db.get_group_list()
    group = Group(name="Test")
    if app.group.count() == 0:
        app.group.create(Group(name=""))
        app.group.edit_first_group(group)
        app.group.delete_first_group()
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
    else:
        l = len(old_groups)
        random_group_index = random.randrange(l)
        group.id = old_groups[random_group_index].id
        if app.group.empty_name(group.id):
            app.open_home_page()
        else:
            app.group.edit_group_by_id(group.id, group)
            new_groups = db.get_group_list()
            assert len(old_groups) == len(new_groups)
            old_groups[random_group_index] = group
            assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
            if check_ui:
                assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                         key=Group.id_or_max)


def test_edit_non_empty_name(app, db, check_ui):
    old_groups = db.get_group_list()
    group = Group(name="")
    if app.group.count() == 0:
        app.group.create(Group(name="Users"))
        app.group.edit_first_group(group)
        app.group.delete_first_group()
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
    else:
        l = len(old_groups)
        random_group_index = random.randrange(l)
        group.id = old_groups[random_group_index].id
        if app.group.empty_name(group.id):
            app.group.edit_group_by_id(group.id, group)
            new_groups = db.get_group_list()
            assert len(old_groups) == len(new_groups)
            old_groups[random_group_index] = group
            assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
            if check_ui:
                assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# тест с индексом

# def test_edit_non_empty_name(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="")
#     if app.group.count() == 0:
#         app.group.create(Group(name="Users"))
#         app.group.edit_first_group(group)
#         app.group.delete_first_group()
#         new_groups = app.group.get_group_list()
#         assert len(old_groups) == len(new_groups)
#     else:
#         index = randrange(len(old_groups))
#         if app.group.empty_name(index):
#             group.id = old_groups[index].id
#             app.group.edit_group_by_index(index, group)
#             assert len(old_groups) == app.group.count()
#             new_groups = app.group.get_group_list()
#             old_groups[index] = group
#             assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
