from domain.factories.make_domain import *
from utils.type import *
from utils.status import *


def test_user_create_event():
    user = make_user()
    user.create_event("event_test", "discussion how to do", IMPORTANCE.IMPORTANT)
    assert user.events[0].status == EventStatus.UNSUBMITTED


def test_user_summit_event():
    user = make_user()
    user.create_event("event_test", "discussion how to do", IMPORTANCE.IMPORTANT)
    user.summit_event(user.events[0])
    assert user.events[0].status == EventStatus.SUBMITTED


def test_user_cancel_event():
    user = make_user()
    user.create_event("event_test", "discussion how to do", IMPORTANCE.IMPORTANT)
    user.cancel_event(user.events[0])
    assert len(user.events) == 0


def test_user_create_vote():
    user = make_user()
    user.create_event("event_test", "discussion how to do", IMPORTANCE.IMPORTANT)

    user.summit_event(user.events[0])

    user.create_vote(user.events[0], ["a", "b", "c"])
    assert user.events[0].status == EventStatus.SUBMITTED
    assert user.votes[0].status == EventStatus.UNSUBMITTED


