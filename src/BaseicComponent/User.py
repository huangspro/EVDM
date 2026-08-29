'''
Define user class.
'''

from datetime import datetime

from Vote import *
from Event import *
from Message import *

class User:
    def __init__(self, name, id, position, status, **kwargs):
        self.name = name
        self.id = id
        self.position = position
        self.status = status
        self.info = kwargs

        # extra info
        self.email = self.info["email"]

        # a user can possess some votes and events
        self.votes = []
        self.events = []
        self.messages = []

    # event related methods
    def create_event(self, name, content, importance):
        t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        newEvent = Event(self, name, content, importance, Status.UNSUBMITTED, self, t)
        self.events.append(newEvent)

    def cancel_event(self, event):
        if event.status != Status.END and event in self.events:
            self.events.remove(event)
            event.cancel()

    # vote related methods
    def create_vote(self, event, options):
        if event.status == Status.SUBMITTED or event.status == Status.UNFINISHED:
            t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            newVote = Vote(self, event, Status.UNSUBMITTED, options, self, t)
            self.votes.append(newVote)

    def cancel_vote(self, targetVote):
        if len(self.votes) > 0 and targetVote in self.votes:
            self.votes.remove(targetVote)
            targetVote.end()

    def begin_vote(self, targetVote):
        if targetVote in self.votes:
            targetVote.begin()


    def end_vote(self, targetVote):
        if targetVote in self.votes:
            targetVote.end()

    # message related methods
    def create_message(self, message):
        self.messages.append(message)

