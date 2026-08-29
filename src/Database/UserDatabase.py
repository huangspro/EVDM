'''
abstract database class for user
'''

from abc import ABC, abstractmethod

class UserDatabase(ABC):
    def __init__(self):
        pass

    # add a user in the database
    @abstractmethod
    def add(self, user):
        pass

    # load a user in the database
    @abstractmethod
    def load_by_username(self):
        pass

    @abstractmethod
    def load_by_password(self):
        pass

    @abstractmethod
    def load_by_email(self):
        pass

    @abstractmethod
    def load_by_id(self):
        pass

    @abstractmethod
    def load_by_position(self):
        pass

    # remove a user
    @abstractmethod
    def remove(self, user):
        pass

    # change the info of a user
    @abstractmethod
    def update(self, user):
        pass