'''
define user class
'''

class Status:
    UNFINISHED = "unfinished"
    FINISHED = "finished"
    UNSUBMITTED = "unsubmitted"
    SUBMITTED = "submitted"
    CANCELED = "canceled"
    HIDE = "hide"
    
    BEGIN = "begin"
    End = "end"
    STOP = "stop"
    ERROR = "error"

    USER_NOT_FOUND = "user_not_found"
    WRONG_PASSWORD = "wrong_password"
    LOGIN_SUCCESSFUL = "login_successful"

    USER_EXISTS = "user_exists"
    REGISTER_SUCCESSFUL = "register_successful"