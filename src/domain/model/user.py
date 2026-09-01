'''
Define user class.
'''

from datetime import datetime

from .vote import Vote
from .event import Event
from utils.status import *
from .message import Message

class User:
    def __init__(self, name:str, id:str, position:str, status:UserStatus, **kwargs):
        self.name = name
        self.ID = id
        self.position = position
        self.status = status
        self.info = kwargs

        # extra info
        self.email = self.info["email"]
        self.phone = self.info["phone"]
        self.organization = self.info["organization"]

        # a user can possess some votes and events
        self.votes = []
        self.events = []
        self.messages = []


    # event related methods
    def create_event(self, name:str, content:str, importance:str):
        t = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        newEvent = Event(name, content, importance, EventStatus.UNSUBMITTED, self, t)
        self.events.append(newEvent)

    def cancel_event(self, event:Event):
        if event.status != EventStatus.CANCELED and event in self.events:
            self.events.remove(event)
            event.status = EventStatus.CANCELED

    def summit_event(self, event:Event):
        if event.status == EventStatus.UNSUBMITTED and event in self.events:
            event.status = EventStatus.SUBMITTED


    # vote related methods
    def create_vote(self, event:Event, options:list):
        if event.status == EventStatus.SUBMITTED:
            t = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            newVote = Vote(event, VoteStatus.UNSUBMITTED, options, self, t)
            self.votes.append(newVote)

    def summit_vote(self, target_vote:Vote):
        if target_vote in self.votes and target_vote.status ==VoteStatus.UNSUBMITTED:
            target_vote.status = VoteStatus.SUBMITTED

    def cancel_vote(self, target_vote):
        if target_vote in self.votes and target_vote.status != VoteStatus.CANCELED:
            self.votes.remove(target_vote)
            target_vote.status = VoteStatus.CANCELED



