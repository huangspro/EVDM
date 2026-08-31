from domain.model.meeting_theme import MeetingTheme
from domain.model.meeting import Meeting

def start_a_meeting_for_theme(meeting_name, user_list):
    new_meeting = MeetingTheme(meeting_name)

    # prepare users for the meeting
    for i in user_list:
        new_meeting.add_user(i)

    return new_meeting

def start_a_vote_for_meeting(current_meeting:Meeting, vote):
    current_meeting.add_vote(vote)
    current_meeting.start_vote(vote)
    current_meeting.end_vote(vote)

    vote_result = current_meeting.get_vote_result(vote)
    current_meeting.conform_thme(vote_result)

    return vote_result

