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
        print(self.__header)
        print(Color.BOLD + "Nýskráning viðskiptavina" + Color.END)
        print("Sláðu inn upplýsingar um viðskiptavin:")
        while True:
            name = input("Nafn: ")
            errorprompt = self.__service.is_valid_name(name)
            if not errorprompt:
                break
            else:
                print(errorprompt)
        while True:
            ssn = input("Kennitala: ")
            errorprompt = self.__service.is_valid_ssn(ssn)
            if not errorprompt:
                break
            else:
                print(errorprompt)
        while True:
            email = input("Netfang: ")
            errorprompt = self.__service.is_valid_email(email)
            if not errorprompt:
                break
            else:
                print(errorprompt)
        while True:
            phoneNr = input("Símanúmer: ")
            errorprompt = self.__service.is_valid_phoneNr(phoneNr)
            if not errorprompt:
                break
            else:
                print(errorprompt)

        NewCustomer = Customer(name, ssn, email, phoneNr)
        self.__service.add_customer(NewCustomer)