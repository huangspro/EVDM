"""
abstract class of meeting
"""


from abc import ABC, abstractmethod


class Meeting(ABC):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    @abstractmethod
    def add_event(self, event):
        pass

    @abstractmethod
    def show_event(self, event):
        pass

    @abstractmethod
    def remove_event(self, event):
        pass

    @abstractmethod
    def add_vote(self, vote):
        pass

    @abstractmethod
    def remove_vote(self, vote):
        pass

    @abstractmethod
    def show_vote(self, vote):
        pass

    @abstractmethod
    def start_vote(self, vote):
        pass

    @abstractmethod
    def end_vote(self, vote):
        pass

    @abstractmethod
    def  get_vote_result(self, vote):
        pass
