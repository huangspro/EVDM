from utils.status import Status


class LoginService:
    def __init__(self, database):
        self.database = database

    def validate_user(self, user, password):
        user_from_database = self.database.find_user_by_attr("id", user.id)
        if len(user_from_database) != 1:
            return Status.USER_NOT_FOUND

        else:
            if password != user_from_database.password:
                return Status.WRONG_PASSWORD
            else:
                return Status.LOGIN_SUCCESSFUL