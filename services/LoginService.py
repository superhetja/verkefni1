from repositories.LoginRepository import LoginRepository

class LoginService(object):

    def __init__(self):
        self.__login_repo = LoginRepository()

    def check_username(self, username):
        '''VEIT EKKI ALVEG HVAÐ ER AÐ GERAST'''
        if self.is_valid(username):
            password = self.__login_repo.get_password(username)
        else:
            return password
            

    def is_valid(self, string):
        #Vantar koda
        pass