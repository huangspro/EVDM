'''
implement database by csv
'''

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

    def insert(self, user):
        pass

    # load a user in the database
    def find_by_username(self):
        pass

    def find_by_password(self):
        pass

    def find_by_email(self):
        pass

    def find_by_id(path, user_id):
    with open(path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["id"] == str(user_id):
                return row

    return None

    def find_by_position(self):
        pass

    # remove a user
    def delete(self, user):
        pass

    # change the info of a user
    def update(self, user):
        pass