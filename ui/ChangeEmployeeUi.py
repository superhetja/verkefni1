from models.Employee import Employee
from ui.HeaderUi imprt Header
from services.EmployeeService import EmployeeService
from models.Clear import Clear

class ChangeEmployeeUi:
    def __init__(self):
        self.__header = Header()
        self.__service = EmployeeService()
        self.__clear = Clear()

    def change_employee(self):
        self.__clear.clear_screen()
        print(self.__header)
        print(Color.BOLD + 'Breyta starfsmanni'+ Color.END)
        print('Sláðu inn upplýsingar um starfsmann')
        while True: 
            