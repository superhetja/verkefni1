from models.Employee import Employee
from ui.HeaderUi import Header
from services.EmployeeService import EmployeeService
from models.Color import Color
from models.Clear import Clear
from ui.Ui import Ui

class CreateEmployee(Ui):
    def __init__(self):
        Ui.__init__(self)
        self.__header = Header()
        self.__service = EmployeeService()
        self.__clear = Clear()
        #self.__input = InputUi()
        
    def create_empoyee(self):
        self.__clear.clear_screen()
        print(self.__header)
        print(Color.BOLD + 'Regester employee'+ Color.END)
        print('Enter employee information')
        name = self.get_string(self.NAMEPROMPT)
        password = input(str("Password: "))
        ssn = self.get_number_length(self.SSNPROMPT, 10)
        email = self.get_email()
        admin = self.get_admin(self.ADMINPROMPT)
        
        new_employee = Employee(name, ssn, password, email, admin)
        self.__service.add_employee(new_employee)