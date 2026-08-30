'''
message is a instance created when users are discussing in the comment section.
'''

from Utils.Type import *

class Message:
    def __init__(self, presenter, present_time, type, status):
        self.presenter = presenter
        self.present_time = present_time
        self.type = type
        self.status = status