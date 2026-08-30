'''
text message
'''

from domain.message import message
from Utils.Type import *

class TextMessage(Message):
    def __init__(self, presenter, present_time, text, status):
        super().__init__(presenter, present_time, MESSAGETYPE.TEXT, status)
        self.text = text