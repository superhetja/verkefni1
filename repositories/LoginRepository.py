
class LoginRepository:

    def __init__(self):
        pass
    
    def get_password(self, username):
        password = None
        with open('data/loginfiles.txt') as aFile:
            fileContent =  [i.split() for i in aFile]
            for i in fileContent:
                if i[0] == username:
                    password = i[1]
            return password
            
