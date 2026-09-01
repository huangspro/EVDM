'''
define Vote class
'''

from .event import Event
from utils.status import *
from .event import *

class Vote:
    def __init__(self, event:Event, status:VoteStatus, options:list, presenter, present_time:str):
        self.event = event
        self.status = status

        self.options = options  # list of strings
        self.options_status = []  # list of numbers
        self.votedUsers = []  # list of users

        self.presenter = presenter
        self.present_time = present_time

    # give an option a vote
    def vote(self, user, option):
        if self.status == VoteStatus.SUBMITTED and user not in self.votedUsers:
            self.options_status[self.options.index(option)] += 1
            self.votedUsers.append(user)

    # calculate out the result of the vote
    def get_result(self):
        tem = self.options_status.index(max(self.options_status))
        return self.options[tem]