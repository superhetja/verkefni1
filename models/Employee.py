class Employee:

    def __init__(self, fullname , ssn, password, email, admin=False):
        """fall sem tekur privit:fullt nafn,kt,lykilorð,email og notendanafn"""
        self.__fullname = fullname
        self.__password = password
        self.__email = email
        self.__admin = admin
        self.__ssn = ssn
    
    def __str__(self):
        """Prentar út"""
        return 'Name: {}, SSN: {}, Email: {}, Password: {}, Admin: {}'.format(self.__fullname, self.__ssn, self.__email, self.__password, self.__admin)    
     
    def __repr__(self):
        """Prentar út upplýsingar fyrir starfsmann"""
        return "Employee('{}','{}','{}','{}','{}')".format(self.__fullname, self.__ssn, self.__email, self.__password, self.__admin)

    def get_fullname(self):
        """Nær í fullt nafn"""
        return self.__fullname
 
    def get_password(self):
        """Nær í lykilorðið"""
        return self.__password

    def get_email(self):
        """Nær í netfangið"""
        return self.__email

    def get_admin(self):
        """Nær í notendanafn"""
        return self.__admin

    def get_ssn(self):
        """Nær í kt."""
        return self.__ssn

