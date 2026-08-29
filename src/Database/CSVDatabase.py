'''
implement database by csv
'''
import csv
import os


class CSVDatabase:
    def __init__(self, path="UserDatabase/Users.csv"):
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
        if self.find_by_email(user.email) is not None:
            return False

        if self.find_by_id(user.ID) is not None:
            return False

        # create new user
        with open(self.path, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([user.name, password, user.ID, user.position, user.status, user.email, user.phone, user.organization])

        return True

    # load a user in the database
    def find_by_name(self, name):
        with open(self.path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            result = []
            for row in reader:
                if row["name"] == str(name):
                    result.append(row)
            return result

        return None

    def find_by_password(self, password):
        with open(self.path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            result = []
            for row in reader:
                if row["password"] == str(password):
                    result.append(row)
            return result
        return None

    def find_by_email(self, email):
        with open(self.path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["email"] == str(email):
                    return row

        return None

    def find_by_id(self, user_id):
        with open(self.path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["id"] == str(user_id):
                    return row

        return None

    def find_by_position(self, position):
        with open(self.path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            result = []
            for row in reader:
                if row["position"] == str(position):
                    result.append(row)
            return result

        return None

    # remove a user
    def delete(self, user):
        pass

    # change the info of a user
    def update(self, user):
        pass