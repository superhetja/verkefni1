from services.CustomerService import CustomerService
from models.Customer import Customer
from models.Color import Color
from ui.HeaderUi import Header
from InputUi import InputUi


class CustomerUi(InputUi):
    def __init__(self):
        self.__service = CustomerService()
        self.__header = Header()

    def new_customer(self):
        print(self.__header)
        print(Color.BOLD + "Nýskráning viðskiptavina" + Color.END)
        print("Sláðu inn upplýsingar um viðskiptavin:")
        name = self.get_string(self.NAMEPROMPT)
        ssn = self.get_valid_numer_lengt(self.SSNPROMPT, 10)
        email = self.get_email()
        phonenr = self.get_valid_numer_lengt(self.PHONEPROMPT,7)
        NewCustomer = Customer(name, ssn, email, phonenr)
        self.__service.add_customer(NewCustomer)