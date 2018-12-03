class Employee:

    def __init__(self, fullname , ssn, password, email, admin=False):
        self.__fullname = fullname
        self.__password = password
        self.__email = email
        self.__admin = admin
        self.__ssn = ssn
    
    def get_fullname(self):
        return self.__fullname

    def get_password(self):
        return self.__username

    def get_email(self):
        return self.__email

    def get_admin(self):
        return self.__admin

    def get_ssn(self):
        return self.__ssn

