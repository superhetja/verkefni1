from models.Employee import Employee
from ui.HeaderUi import Header
from services.EmployeeService import EmployeeService
from models.Color import Color
from models.Clear import Clear

class CreateEmployeeUi:
    def __init__(self):
        self.__header = Header()
        self.__service = EmployeeService()
        self.__clear = Clear()
        
    def create_empoyee(self):
        self.__clear.clear_screen()
        print(self.__header)
        print(Color.BOLD + 'Nýskráning starfsmanna'+ Color.END)
        print('Sláðu inn upplýsingar um starfsmann')
        while True:
            fullname = input('Fullt nafn: ')
            errorprompt = self.__service.is_valid_fullname(fullname)
            if not errorprompt:
                break
            else:
                print(errorprompt)    
        password = input(str('Lykilorð: '))
        while True:
            ssn = input('Kennitala: ')
            errorprompt = self.__service.is_valid_ssn(ssn)
            if not errorprompt:
                break
            else:
                print(errorprompt)
        while True:
            email = input('Email: ')
            errorprompt = self.__service.is_valid_email(email)
            if not errorprompt:
                break
            else:
                print(errorprompt)
        while True:
            admin = input('Admin y/n: ').capitalize()
            errorprompt = self.__service.is_valid_admin(admin)
            if not errorprompt:
                break
            else:
                print(errorprompt)

        new_employee = Employee(fullname, ssn, password, email, admin)