from utils.status import Status


class LoginService:
    def __init__(self, database, authentication_validator):
        self.database = database
        self.authentication_validator = authentication_validator

    def validate_user(self, user, password):
        if self.authentication_validator.validate_user_by_email(user.email) is False:
            return Status.AUTHENTICATION_FAILED

        else:
            user_from_database = self.database.find_user_by_attr("id", user.id)
            if len(user_from_database) != 1:
                return Status.USER_NOT_FOUND

            else:
                if password != user_from_database.password:
                    return Status.WRONG_PASSWORD
                else:
                    return Status.LOGIN_SUCCESSFUL