'''
message is a instance created when users are discussing in the comment section.
'''

from utils.type import *

class Message:
    def __init__(self, presenter, present_time, type, status):
        self.presenter = presenter
        self.present_time = present_time
        self.type = type
        self.status = status


class PictureMessage(Message):
    def __init__(self, presenter, present_time, picture_path, status):
        super().__init__(presenter, present_time, MESSAGETYPE.PICTURE, status)
        self.picture_path = picture_path

    def load(self):
        pass


class TextMessage(Message):
    def __init__(self, presenter, present_time, text, status):
        super().__init__(presenter, present_time, MESSAGETYPE.TEXT, status)
        self.text = text