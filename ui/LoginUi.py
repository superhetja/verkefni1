from services import LoginService

class Login:

    def __init__(self):
        self.__login_service = LoginService()

    def login_menu(self):
        while True:
            username = input('Notendanafn: ')
            try: 
                self.__login_service.__check_username(username)

        while True:       
            password = input('Lykilorð: ')
            if password:
                break

