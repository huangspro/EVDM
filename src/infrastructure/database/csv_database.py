'''
implement database by csv
'''
import csv
import os

from domain.repository.user_database import UserDatabase
from domain.model.user import User

class CSVDatabase(UserDatabase):

    def __init__(self, path="UserDatabase/Users.csv"):
        super().__init__()
        self.path = path

        # create directory
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

        # create csv file
        if not os.path.exists(self.path):
            with open(self.path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["name", "password", "id", "position", "status", "email", "phone", "organization"])

    def insert(self, user, password):
        # check if email or id exists
        if len(self.find_user_by_attr("email", user.email)) != 0:
            return False

        if len(self.find_user_by_attr("id", user.ID)) != 0:
            return False

        # create new user
        with open(self.path, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([user.name, password, user.ID, user.position, user.status, user.email, user.phone, user.organization])

        return True

    # load a user in the database
    def find_user_by_attr(self, attr_name, attr_value):
        with open(self.path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            result = []
            for row in reader:
                if row[str(attr_name)] == str(attr_value):
                    result.append(row)
            return result

        return None

    # remove a user
    def delete(self, user):
        pass

    # change the info of a user
    def update(self, user):
        pass