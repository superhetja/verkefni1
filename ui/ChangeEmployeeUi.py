from models.Employee import Employee
from ui.HeaderUi import Header
from services.EmployeeService import EmployeeService
from models.Clear import Clear
from ui.Ui import Ui
from models.Color import Color

class ChangeEmployeeUi:
    def __init__(self):
        Ui.__init__(self)
        self.__header = Header()
        self.__service = EmployeeService()
        self.__clear = Clear()
        #self.__input = InputUi()

    def change_employee(self, employee):
        action = self.main_menu()
        if action == '1':
            name = self.get_string(self.NAMEPROMPT)
        elif action == '2':
            email = self.get_email()
        elif action == '3':
            ssn = self.get_number_length(self.SSNPROMPT, 10)
        elif action == '4':
            admin = self.get_admin(self.ADMINPROMPT)
        changedEmployee = Employee(name, email, ssn, admin, password)
        self.__service.remove_employee(employee)
        self.__service.add_employee(changedEmployee)

    def main_menu(self):
        print(Color.BOLD + 'Starfsmaður'+ Color.END)
        print('1. Breyta nafni')
        print('2. Breyta netfangi')
        print('3. Breyta kennitölu')
        print('4. Breyta stöðu')
        print('5. Breyta lykilorði')

        action = self.get_number_between(1, 5)
        return action 