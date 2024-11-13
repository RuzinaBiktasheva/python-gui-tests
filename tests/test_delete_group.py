from models.group import Group
from random import randrange


# тест на удаление группы по индексу
def test_delete_group_by_index(app):
    if app.group.count() <= 1:
        app.group.add_group(Group('New group for delete'))
    old_list = app.group.get_group_list()
    app.group.delete_group_by_index(0)
    new_list = app.group.get_group_list()
    del old_list[0:1]
    assert sorted(old_list) == sorted(new_list)

# тест на удаление произвольной группы
def test_delete_random_group(app):
    if app.group.count() <= 1:
        app.group.add_group(Group('New group for delete'))
    old_list = app.group.get_group_list()
    index = randrange(0, app.group.count())
    app.group.delete_random_group(index)
    new_list = app.group.get_group_list()
    del old_list[index:index+1]
    for i in range(app.group.count()):
        print("Old: ", i, old_list[i], "New: ", i, new_list[i])
    assert sorted(old_list) == sorted(new_list)