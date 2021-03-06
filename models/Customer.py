class Customer:
    def __init__(self, name='', ssn=0, email='', phoneNr=''):
        self.__name = name
        self.__email = email
        self.__ssn = ssn
        self.__phoneNr = phoneNr

    def __str__(self):
        '''Prentar út strengi, nafn, kt.,netfang,símanr.'''
        return 'Name: {:40} \tSSN: {} \n\tEmail: {:40} Phone number: {}'.format(self.__name, self.print_ssn(), self.__email, self.print_phone())    
     
    def __repr__(self):
        '''Prentar út upplýsingar um viðskiptavin'''
        return "Customer('{}','{}','{}','{}')".format(self.__name, self.__ssn, self.__email, self.__phoneNr)

    def print_ssn(self):
        '''Gerir kennitöluprentanlegri'''
        ssn = self.__ssn[:6]+'-'+self.__ssn[6:]
        return ssn
    
    def print_phone(self):
        phoneNr = self.__phoneNr[:3]+'-'+self.__phoneNr[3:]
        return phoneNr

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_ssn(self):
        return self.__ssn

    def get_phoneNr(self):
        return self.__phoneNr
    
    def get_id(self):
        return self.__ssn