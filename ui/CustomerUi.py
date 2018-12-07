from services.CustomerService import CustomerService
from models.Customer import Customer
from models.Color import Color
from ui.HeaderUi import Header
from ui.InputUi import InputUi

class CustomerUi:
    def __init__(self):
        self.__service = CustomerService()
        self.__header = Header()
        self.__input = InputUi()

    def new_customer(self):
        print(self.__header)
        print(Color.BOLD + "Nýskráning viðskiptavina" + Color.END)
        print("Sláðu inn upplýsingar um viðskiptavin:")
        name = self.__input.get_string(self.__input.NAMEPROMPT)
        ssn = self.__input.get_number_length(self.__input.SSNPROMPT, 10)
        email = self.__input.get_email()
        phonenr = self.__input.get_number_length(self.__input.PHONEPROMPT,7)
        NewCustomer = Customer(name, ssn, email, phonenr)
        self.__service.add_customer(NewCustomer)