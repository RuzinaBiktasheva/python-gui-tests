import pytest
from fixtures.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("D:/Programms/Addressbook/AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture
