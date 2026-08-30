'''
define Vote class
'''

from .event import Event
from utils.status import Status

class Vote:
    def __init__(self, event, status, options, presenter, present_time):
        self.event = event
        self.status = status

        self.options = options  # list of string
        self.options_status = []  # list of number
        self.votedUsers = []

        self.presenter = presenter
        self.present_time = present_time

    # begin a vote
    def begin(self):
        self.status = Status.BEGIN

    # end a vote
    def end(self):
        self.status = Status.END

    # give an option a vote
    def add(self, user, option):
        if self.status == Status.BEGIN and user not in self.votedUsers:
            self.options_status[self.options.index(option)] += 1
            self.votedUsers.append(user)

    # calculate out the result of the vote
    def result(self):
        tem = self.options_status.index(max(self.options_status))
        return self.options[tem]