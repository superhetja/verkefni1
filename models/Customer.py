class Customer:
    def __init__(self, name='', ssn=0, email='', phoneNr=''):
        self.__name = name
        self.__email = email
        self.__ssn = ssn
        self.__phoneNr = phoneNr

    def __str__(self):
        '''Prentar út strengi, nafn, kt.,netfang,símanr.'''
        return 'Name: {}, SSN: {}, Email: {}, Phone number: {}'.format(self.__name, self.__ssn, self.__email, self.__phoneNr)    
     
    def __repr__(self):
        '''Prentar út upplýsingar um viðskiptavin'''
        return "Customer('{}','{}','{}','{}')".format(self.__name, self.__ssn, self.__email, self.__phoneNr)

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_ssn(self):
        return self.__ssn

    def get_phoneNr(self):
        return self.__phoneNr 