'''
abstract database class for user
'''

from abc import ABC, abstractmethod


class UserDatabase(ABC):
    def __init__(self):
        pass

    # add a user in the database
    @abstractmethod
    def insert(self, user, password):
        pass

    # find a user in the database
    @abstractmethod
    def find_user_by_attr(self, attr_name, attr_value):
        pass

    # change the info of a user
    @abstractmethod
    def update(self, user):
        pass

    # delete a user
    @abstractmethod
    def delete(self, user):
        pass