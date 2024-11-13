class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list

    def add_group(self, group):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(group.name)
        input.type_keys("\n")
        self.close_group_editor()

    def delete_group_by_index(self, index):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        root.children()[index].click() # выбор элемента в списке
        self.group_editor.window(auto_id="uxDeleteAddressButton").click() # нажатие на кнопку "Delete"
        self.group_delete = self.app.application.window(title="Delete group") # модальное окно удаления группы
        self.group_delete.window(auto_id="uxDeleteAllRadioButton").click()  # выбор радиокнопки
        self.group_delete.window(auto_id="uxOKAddressButton").click() # нажатие на кнопку "ОК"
        self.close_group_editor()

    def delete_random_group(self, index):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        root.children()[index].click() # выбор элемента в списке
        self.group_editor.window(auto_id="uxDeleteAddressButton").click() # нажатие на кнопку "Delete"
        self.group_delete = self.app.application.window(title="Delete group") # модальное окно удаления группы
        self.group_delete.window(auto_id="uxDeleteAllRadioButton").click()  # выбор радиокнопки
        self.group_delete.window(auto_id="uxOKAddressButton").click() # нажатие на кнопку "ОК"
        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def count(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return len(group_list)

    def close_group_editor(self):
        self.group_editor.close()