from models.Employee import Employee
from ui.HeaderUi imprt Header
from services.EmployeeService import EmployeeService
from models.Clear import Clear
from ui.InputUi import InputUi

class ChangeEmployeeUi:
    def __init__(self):
        self.__header = Header()
        self.__service = EmployeeService()
        self.__clear = Clear()
        self.__get_input = InputUi

    def change_employee(self):
        name = self.__get_input.get_name(self.__get_input.NAMEPROMPT)
        email = self.__get_input.get_email(self.__get_input.EMAILPROMPT)
        ssn = self.__get_input.get_ssn(self.__get_input.SSNPROMPT)
        admin = self.__get_input.get_admin(self.__get_input.ADMINPROMPT)
        password = input('Lykilorð: ')

    def __init__(self):
        self.__check_input = CheckInput()

    def 
        
        
            