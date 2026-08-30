'''
Define the Event class
'''

from Utils.Status import *


class Event:
    def __init__(self, name, content, importance, status, presenter, present_time):
        self.name = name
        self.content = content
        self.importance = importance  # common, important, nontrivial
        self.status = status  # unfinished, finished, submitted, unsubmitted, canceled

        self.presenter = presenter
        self.present_time = present_time

    def cancel(self):
        self.status = Status.UNSUBMITTED