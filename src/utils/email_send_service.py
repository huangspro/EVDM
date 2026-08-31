from abc import ABC, abstractmethod


class EmailSendService(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def send_email_of_text(self, text_content, from_address, to_address, subject):
        pass