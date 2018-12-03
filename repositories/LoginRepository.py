
class LoginRepositry:

    def __init__(self):
        pass
    
    def get_username(self, username):
        with open('data/loginfiles.txt') as aFile:
            fileContent =  [i.split() for i in aFile]
            print(fileContent)


a = LoginRepositry()
a.get_username('kalli')