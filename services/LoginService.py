from repositories import LoginRepository

class LoginRepository():

    def __init__(self):
        self.__login_repo = LoginRepository()

    def check_username(self, username):
        if self.is_valid(username):
            self.__login_repo.get_username(username)

    def is_valid(self, string):
        #Vantar koda
        pass
