import pytest
from fixtures.application import Application
import pandas as pd
import jsonpickle
import os
from models.group import Group


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("D:/Programms/Addressbook/AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith('json_'):
            testdata = load_from_json()
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith('excel_'):
            testdata = load_from_excel()
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


# чтение данных из json
def load_from_json():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/groups.json')) as f:
        return jsonpickle.decode(f.read())

# чтение данных из excel
def load_from_excel():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/groups.xlsx')
    df = pd.read_excel(file_path, header=None)
    list = []
    for _, row in df.iterrows():
        row_string = row.to_string(index=False)
        list.append(Group(name=row_string))
    return list