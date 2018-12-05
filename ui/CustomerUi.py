from services.CustomerService import CustomerService
from models.Customer import Customer
from HeaderUi import Color
import HeaderUi

HeaderUi.print_header()
class Customer:
    def __init__(self):
        self.__customer_service = CustomerService()

    def new_customer(self):
        print(Color.BOLD + "Nýskráning viðskiptavina" + Color.END)
        print("Upplýsingar um viðskiptavin:")
        name = input("Nafn: ")
        ssn = input("Kennitala: ")
        email = input("Netfang: ")
        phoneNr = input("Símanúmer: ")
        NewCustomer = Customer(name, ssn, email, phoneNr)
        self.__customer_service.add_customer(NewCustomer)

    def get_another_input(self, errorpromt, inputprompt):
        print(errorpromt)
        new_input = input()
        return new_input