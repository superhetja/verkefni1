from services.LoginService import LoginService

class Login:

    def __init__(self):
        self.__login_service = LoginService()

    def login_menu(self):
        while True:
            while True:
                username = input('Username: ')
                password_from_file = self.__login_service.check_username(username)
                if password_from_file:
                    break
            password = input('Password:')
            if password == password_from_file:
                break



