'''
message with picture
'''

from domain.message import message
from utils.type import *

class PictureMessage(message.Message):
    def __init__(self, presenter, present_time, picture_path, status):
        super().__init__(presenter, present_time, MESSAGETYPE.PICTURE, status)
        self.picture_path = picture_path

    def load(self):
        pass