from services.CustomerService import CustomerService
from models.Customer import Customer
from models.Color import Color
from ui.HeaderUi import Header


class CustomerUi:
    def __init__(self):
        self.__service = CustomerService()
        self.__header = Header()

    def print_all_customers(self):
        customers = self.__service.get_customers()
        for customer in customers:
            print(customer)

    def new_customer(self):
        print(Header())
        print(Color.BOLD + "Nýskráning viðskiptavina" + Color.END)
        print("Sláðu inn upplýsingar um viðskiptavin:")
        name = input("Nafn: ")
        ssn = input("Kennitala: ")
        email = input("Netfang: ")
        phoneNr = input("Símanúmer: ")
        NewCustomer = Customer(name, ssn, email, phoneNr)
        self.__service.add_customer(NewCustomer)

    def get_another_input(self, errorpromt, inputprompt):
        print(errorpromt)
        new_input = input()
        return new_input