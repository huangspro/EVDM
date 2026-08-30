from infrastructure.database.csv_database import CSVDatabase
from domain.model.user import User
from domain.factories import make_domain

def test_initialize_a_database():
    db = CSVDatabase("UserDatabase/Users.csv")


def test_insert_user_to_database():
    newone = make_domain.make_user()
    db = CSVDatabase("UserDatabase/Users.csv")
    db.insert(newone, "123456")


def test_find_user_by_attr():
    db = CSVDatabase("UserDatabase/Users.csv")
    assert len(db.find_user_by_attr("email", "13612276628@163.com")) != 0
    assert len(db.find_user_by_attr("phone", "1362262")) == 0
