'''
implement database by csv
'''

class CSVDatabase:
    def __init__(self, path = "UserDatabase/Users.csv"):
        self.path = path

    def add(self, user):
        pass

    # load a user in the database
    def load_by_username(self):
        pass

    def load_by_password(self):
        pass

    def load_by_email(self):
        pass

    def load_by_id(self):
        pass

    def load_by_position(self):
        pass

    # remove a user
    def remove(self, user):
        pass

    # change the info of a user
    def update(self, user):
        pass