from utils.status import Status


class RegisterService:
    def __init__(self, database):
        self.database = database


    def validate(self, user):
        user_from_email = self.database.find_user_by_attr("email", user.email)
        user_from_id = self.database.find_user_by_attr("id", user.password)

        if len(user_from_email) != 0 or len(user_from_id) != 0:
            return Status.USER_EXISTS
        else:
            self.database.insert_user(user)
            return Status.REGISTER_SUCCESSFUL