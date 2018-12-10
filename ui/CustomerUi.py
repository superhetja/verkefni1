from services.CustomerService import CustomerService
from models.Customer import Customer
from models.Color import Color
from ui.HeaderUi import Header
from ui.Ui import Ui

class CustomerUi:
    def __init__(self):
        Ui.__init__(self)
        self.__service = CustomerService()
        self.__header = Header()
        #self.__input = Ui()

    def new_customer(self):
        print(self.__header)
        print(Color.BOLD + "Nýskráning viðskiptavina" + Color.END)
        print("Sláðu inn upplýsingar um viðskiptavin:")
        name = self.get_string(self.NAMEPROMPT)
        ssn = self.get_number_length(self.SSNPROMPT, 10)
        email = self.get_email()
        phonenr = self.get_number_length(self.PHONEPROMPT,7)
        NewCustomer = Customer(name, ssn, email, phonenr)
        self.__service.add_customer(NewCustomer)