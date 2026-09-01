'''
Define the Event class
'''

from utils.status import *
from utils.type import *


class Event:
    def __init__(self, name:str, content:str, importance:IMPORTANCE, status:EventStatus, presenter, present_time:str):
        self.name = name
        self.content = content
        self.importance = importance  # common, important, nontrivial
        self.status = status  # unfinished, finished, submitted, unsubmitted, canceled

        self.presenter = presenter
        self.present_time = present_time