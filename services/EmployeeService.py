from repositories.EmployeeRepository import EmployeeRepository
from services.CheckInputService import CheckInput


class EmployeeService:

    def __init__(self):
        self.__check_input = CheckInput()

    def add_employee(self, employee):
        pass


    def is_valid_employee(self, employee):
        # self.__fullname = fullname
        # self.__password = password
        # self.__email = email
        # self.__admin = admin
        # self.__ssn = ssn
        pass
#nafn
    def is_valid_fullname(self,fullname):
        return self.__check_input.is_string(fullname)

#password
  


#email
    def is_valid_email(self, email):
        errorprompt = 'Rangt netfang\nSláðu inn gilt netfang.'
        try:
            atsymbol = email.index('@')
            email.index('.', atsymbol)
            return None
        except ValueError:
            return errorprompt
#admin 
    def is_valid_admin(self, admin):
        return self.__check_is_valid_between_two_letters('y,n')
        
#ssn
    def is_valid_ssn(self, ssn):
        return self.__check_input.is_valid_number_length(ssn,10)
            


