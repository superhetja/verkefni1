from services.CustomerService import CustomerService
from models.Customer import Customer
from models.Color import Color
from ui.HeaderUi import Header
from ui.Ui import Ui

class CustomerUi(Ui):
    def __init__(self):
        Ui.__init__(self)
        self.__service = CustomerService()
        self.__header = Header()

    def customer_main(self):
        '''synir main fallid'''
        print(self.__header)
        self.clear_screen()
        print(Color.BOLD + "Register customer" + Color.END)
        self.new_customer()
        self.get_more()

    def new_customer(self):
        '''baetir vid nyjum vidskiptavini'''
        print("Enter customer information")
        name = self.get_string(self.NAMEPROMPT)
        ssn = self.get_number_length(self.SSNPROMPT, 10)
        email = self.get_email()
        phonenr = self.get_number_length(self.PHONEPROMPT,7)
        NewCustomer = Customer(name, ssn, email, phonenr)
        self.__service.add_content(NewCustomer)
        print(Color.GREEN + 'Customer registered' + Color.END)

    def get_more(self):
        '''Spyr notenda um meira hvort hann vilji halda afram'''
        letter = self.get_letter(self.MOREPROMPT,['y','n'])
        if letter == 'y':
            self.customer_main()
        else:
            pass