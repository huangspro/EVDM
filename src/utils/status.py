'''
define user class
'''

class UserStatus:
    ON_MEETING = "on_meeting"
    OFF_MEETING = "off_meeting"

class LoginStatus:
    USER_NOT_FOUND = "user_not_found"
    WRONG_PASSWORD = "wrong_password"

    LOGIN_SUCCESSFUL = "login_successful"
    LOGIN_FAILED = "login_failed"

    USER_EXISTS = "user_exists"
    EMAIL_EXISTS = "email_exists"

    REGISTER_SUCCESSFUL = "register_successful"
    REGISTER_FAILED = "register_failed"

    AUTHENTICATION_FAILED = "authentication_failed"

    TIMEOUT = "timeout"

class VoteStatus:
    UNSUBMITTED = "unsubmitted"
    SUBMITTED = "submitted"
    GOING = "going"
    FINISHED = "finished"
    CANCELED = "canceled"

class EventStatus:
    UNSUBMITTED = "unsubmitted"
    SUBMITTED = "submitted"
    GOING = "going"
    FINISHED = "finished"
    CANCELED = "canceled"

class MessageStatus:
    UNSUBMITTED = "unsubmitted"
    SUBMITTED = "submitted"
