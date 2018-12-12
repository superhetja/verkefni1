from services.CustomerService import CustomerService
from services.CheckInputService import CheckInput
from models.Customer import Customer
from ui.HeaderUi import Header
#from models.Clear import Clear
from models.Color import Color
from ui.Ui import Ui


class ShowCustomer(Ui):
    def __init__(self):
        Ui.__init__(self)
        self.__service = CustomerService()
        self.__header = Header()
        self.__color = Color()
        self.__check_input = CheckInput()

    def search_customer(self):
        '''leitar ad vidskiptavini med tvi ad setja inn nafnid'''
        self.clear_screen()
        print(Color.BOLD+'Search customer'+Color.END)
        search = input('Input search: ').lower()
        customers = self.__service.get_matches(search)
        self.print_list(customers)
        if len(customers) == 0:
            self.get_more()
        else:
            self.choose_customer(customers)

    def print_all_customers(self):
        '''prentar ut alla vidskiptavini'''
        self.clear_screen()
        print(Color.BOLD + 'Yfirlit yfir viðskiptavini' + Color.END)
        customers = self.__service.get_full_content()
        self.print_list(customers)
        self.choose_customer(customers)

    def choose_customer(self, a_list):
        '''velja vidskiptavin og moguleikar um ad velja fleira'''
        choice = self.get_number_between(1,len(a_list)+1)
        chosen_customer = a_list[int(choice)-1]
        print(chosen_customer)
        print('1. Delete customer')
        print('2. Change customer')
        print('3. Search another customer')
        print('4. Back to main menu')
        action = self.get_number_between(1,4)
        if action == '1':
            self.__service.remove_instance(chosen_customer)
            print('Customer deleted')
            self.get_more()
        elif action == '2':
            self.change_customer(chosen_customer)
        elif action == '3':
            self.search_customer()
        else:
            pass
    
    def change_customer(self, customer):
        '''breytir upplysingum um vidskiptavini'''
        print('What do you want to change?')
        print('1. Name')
        print('2. SSN')
        print('3. Email')
        print('4. Phone number')
        action = self.get_number_between(1,4)
        name = customer.get_name()
        ssn = customer.get_ssn()
        email = customer.get_email()
        phonenr = customer.get_phoneNr()
        if action == '1':
            name = self.get_string(self.NAMEPROMPT)
        elif action == '2':
            ssn = self.get_number_length(self.SSNPROMPT,10)
        elif action == '3':
            email = self.get_email()
        else:
            phonenr = self.get_number_length(self.PHONEPROMPT,7)
        new_customer= Customer(name,ssn,email,phonenr)
        self.__service.change_instance(customer, new_customer)
        print('Change complete')
        self.get_more()

    def get_more(self):
        '''Spyr notenda um meira hvort hann vilji halda afram'''
        letter = self.get_letter(self.MOREPROMPT,['y','n'])
        if letter == 'y':
            self.search_customer()
        else:
            pass
