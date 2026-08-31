from .meeting import Meeting
from utils.type import MEETINGTYPE

class MeetingTheme(Meeting):
    def __init__(self, name):
        super().__init__(name, MEETINGTYPE.THEME)
        self.theme = ""
        self.event = []
        self.vote = []
        self.users = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)

    def add_event(self, event):
        if event not in self.event:
            self.event.append(event)


    def show_event(self, event):
        pass


    def remove_event(self, event):
        if event in self.event:
            self.event.remove(event)


    def add_vote(self, vote):
        if vote not in self.vote:
            self.vote.append(vote)


    def remove_vote(self, vote):
        if vote in self.vote:
            self.vote.remove(vote)


    def show_vote(self, vote):
        pass


    def start_vote(self, vote):
        if vote in self.vote:
            vote.begin()


    def end_vote(self, vote):
        if vote in self.vote:
            vote.end()


    def get_vote_result(self, vote):
        if vote in self.vote:
            self.theme = vote.result
            return vote.result()

    def confirm_theme(self, final_theme):
        self.theme = final_theme