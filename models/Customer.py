class Customer:
    def __init__(self, name='', ssn=0, email='', phoneNr=''):
        self.__name = name
        self.__email = email
        self.__ssn = ssn
        self.__phoneNr = phoneNr
    
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_ssn(self):
        return self.__ssn

    def get_phoneNr(slef):
        return self.__phoneNr