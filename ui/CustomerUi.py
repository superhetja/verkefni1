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
        #self.__input = Ui()

    def customer_main(self):
        '''synir main fallid'''
        print(self.__header)
        print(Color.BOLD + "Register customer" + Color.END)
        self.new_customer()

    def new_customer(self):
        '''baetir vid nyjum vidskiptavini'''
        print("Enter custumer information")
        name = self.get_string(self.NAMEPROMPT)
        ssn = self.get_number_length(self.SSNPROMPT, 10)
        email = self.get_email()
        phonenr = self.get_number_length(self.PHONEPROMPT,7)
        NewCustomer = Customer(name, ssn, email, phonenr)
        self.__service.add_content(NewCustomer)
        print('Customer registered')