from models.Employee import Employee
from ui.HeaderUi import Header
from services.EmployeeService import EmployeeService
from models.Color import Color
from models.Clear import Clear
from ui.InputUi import InputUi

class CreateEmployeeUi:
    def __init__(self):
        self.__header = Header()
        self.__service = EmployeeService()
        self.__clear = Clear()
        self.__input = InputUi()
        
    def create_empoyee(self):
        self.__clear.clear_screen()
        print(self.__header)
        print(Color.BOLD + 'Nýskráning starfsmanna'+ Color.END)
        print('Sláðu inn upplýsingar um starfsmann')
        name = self.__input.get_string(self.__input.NAMEPROMPT)
        password = input(str("Lykilorð: "))
        ssn = self.__input.get_number_length(self.__input.SSNPROMPT, 10)
        email = self.__input.get_email()
        admin = self.__input.get_admin(self.__input.ADMINPROMPT)
        
        new_employee = Employee(name, ssn, password, email, admin)
        self.__service.add_employee(new_employee)