from models.group import Group
from data.group_data import data



# тест на добавление группы из файла data.group_data.py
def test_add_group(app):
    group = data
    old_list = app.group.get_group_list()
    app.group.add_group(group)
    new_list = app.group.get_group_list()
    old_list.append(group)
    assert sorted(new_list) == sorted(new_list)

# тест на добавление группы
#def test_add_group(app):
    #group = Group('New add group 5')
    #old_list = app.group.get_group_list()
    #app.group.add_group(group)
    #new_list = app.group.get_group_list()
    #old_list.append(group)
    #assert sorted(new_list) == sorted(new_list)