from infrastructure.database.CSVDatabase import CSVDatabase
from BaseicComponent.User import User


def test_initialize_a_database():
    db = CSVDatabase("UserDatabase/Users.csv")


def test_insert_user_to_database():
    newone = User("newone", "104523", "teacher", "formal", email="13612276628@163.com", phone="13546259795", organization="ASchool")
    db = CSVDatabase("UserDatabase/Users.csv")
    db.insert(newone, "123456")


def test_find_user_by_email():
    db = CSVDatabase("UserDatabase/Users.csv")
    assert db.find_by_email("13612276628@163.com") is not None
    assert db.find_by_email("1362262") is None

def test_find_user_by_name():
    db = CSVDatabase("UserDatabase/Users.csv")
    assert db.find_by_name("newone") is not None
    assert len(db.find_by_name("hello")) == 0

def test_find_user_by_id():
    db = CSVDatabase("UserDatabase/Users.csv")
    assert db.find_by_id(104523) is not None
    assert db.find_by_id(2) is None

def test_find_user_by_position():
    db = CSVDatabase("UserDatabase/Users.csv")
    assert db.find_by_position(104523) is not None
    assert len(db.find_by_position(2)) == 0