from models.group import Group


# тест на добавление группы
def test_add_group(app):
    group = Group('New add group 5')
    old_list = app.group.get_group_list()
    app.group.add_group(group)
    new_list = app.group.get_group_list()
    old_list.append(group)
    assert sorted(new_list) == sorted(new_list)