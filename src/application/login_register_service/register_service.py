from utils.status import Status


class RegisterService:
    def __init__(self, database, authentication_validator):
        self.database = database
        self.authentication_validator = authentication_validator

    def validate(self, user):
        if self.authentication_validator.validvalidate_user_by_emailate_user(user):
            return Status.REGISTER_SUCCESSFUL

        else:
            user_from_email = self.database.find_user_by_attr("email", user.email)
            user_from_id = self.database.find_user_by_attr("id", user.password)

            if len(user_from_email) != 0 or len(user_from_id) != 0:
                return Status.USER_EXISTS
            else:
                self.database.insert_user(user)
                return Status.REGISTER_SUCCESSFUL