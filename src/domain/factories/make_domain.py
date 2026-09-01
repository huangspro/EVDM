from domain.model.user import User
from domain.model.vote import Vote
from domain.model.event import Event
from utils.status import *
from utils.type import *

def make_user():
    newone = User("newone", "104523", "teacher", "formal", email="13612276628@163.com", phone="13546259795", organization="ASchool")
    return newone

def make_event(user):
    newone = Event("event1", "how to do", IMPORTANCE.IMPORTANT, EventStatus.UNSUBMITTED, user, "2026-1-10")
    return newone

def make_vote(event, user):
    newone = Vote(event, VoteStatus.UNSUBMITTED, ["a", "b", "c"], user, "2026-1-21")