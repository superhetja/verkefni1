from models.Employee import Employee
from HeaderUi import Header
from services.EmployeeService import EmployeeService
from models.Color import Color
from models.Clear import Clear
from Ui import Ui

class CreateEmployee:
    def __init__(self):
        Ui.__init__(self)
        self.__header = Header()
        self.__service = EmployeeService()
        self.__clear = Clear()
        #self.__input = InputUi()
        
    def create_empoyee(self):
        self.__clear.clear_screen()
        print(self.__header)
        print(Color.BOLD + 'Nýskráning starfsmanna'+ Color.END)
        print('Sláðu inn upplýsingar um starfsmann')
        name = self.get_string(self.NAMEPROMPT)
        password = input(str("Lykilorð: "))
        ssn = self.get_number_length(self.SSNPROMPT, 10)
        email = self.get_email()
        admin = self.get_admin(self.ADMINPROMPT)
        
        new_employee = Employee(name, ssn, password, email, admin)
        self.__service.add_employee(new_employee)