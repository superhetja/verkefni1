from services.EmployeeService import EmployeeService
from services.CheckInputService import CheckInput
from models.Customer import Customer
from ui.HeaderUi import Header
#from models.Clear import Clear
from models.Color import Color
from ui.Ui import Ui
from services.Service import Service


class ShowEmployee(Ui):
    def __init__(self):
        Ui.__init__(self)
        self.__employee_service = EmployeeService()
        self.__service = Service()
        self.__header = Header()
        self.__check_input = CheckInput()

    def print_menu(self):
        print(Color.BOLD+'Search employee'+Color.END)
        print('1. Search employee')
        print('2. View all employees')

    def show_employee_main(self):
        #eftir .........
        '''Aðal fallið til að byrja klassan'''
        self.clear_screen()
        self.print_menu()
        action = self.get_number_between(1,2) #self.get_number_between(1,5)
        if action == '1':
            self.search_customer()
        else:
            self.print_all_customers()
    #---------------------------------------------


    def search_employee(self):
        search = input('Input search: ')
        employee = self.__employee_service.get_matches(search)
        self.print_list(employee)
        if len(employee) == 0:
            self.get_more()
        else:
            self.choice_employeer(employee)

    def print_all_employees(self):
        employee = self.__employee_service.get_full_centent()
        self.print_lisr(employee)
        if len(employee) == 0:
            self.get_more()
        else:
            self.choice_employee(employee)

    # def get_more(self):
    #     letter = self.get_letter(self.MOREPROMPT,['j','n'])
    #     if letter == 'j':
    #         self.show_employee_main()
    #     else:
    #         pass

    def choose_employee(self, a_list):
        choice = self.get_number_between(1,len(a_list)+1)
        chosen_employee = a_list[int(choice)-1]
        print(chosen_employee)
        print('1. Change employee')
        print('2. Delete employee')
        print('3. Search another employee')
        print('4. Back to menu')
        action = self.get_number_between(1,4)
        if action == '1':
            self.__service.remove_instance(chosen_employee)
            print('Employee deleted')
            self.get_more()
        elif action == '2':
            self.__change_employee(chosen_employee)
        elif action == '3':
            self.show_employee_main()
        else:
            pass
    
    def __change_employee(self, employee):
        print('What do you want to change?')
        print('1. Name')
        print('2. Ssn')
        print('3. Email')
        print('4. Phone number')
        action = self.get_number_between(1,4)
        name = employee.get_name()
        ssn = employee.get_ssn()
        email = employee.get_email()
        phonenr = employee.get_phoneNr()
        if action == '1':
            name = self.get_string(self.NAMEPROMPT)
        elif action == '2':
            ssn = self.get_number_length(self.SSNPROMPT,10)
        elif action == '3':
            email = self.get_email()
        else:
            phonenr = self.get_number_length(self.PHONEPROMPT,7)
        new_employee= employee(name,ssn,email,phonenr)
        self.__service.change_instance(employee, new_employee)
        print('Change complete!')
        self.get_more()