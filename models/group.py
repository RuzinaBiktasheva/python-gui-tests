class Group:

    def __init__(self, name = None):
        self.name = name

    # переопределенная стандартная функция представления
    def __repr__(self):
        return '%s' % (self.name)

    # переопределенная стандартная функция сравнения
    def __eq__(self, other):
        return self.name == other.name