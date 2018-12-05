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
        while True:
            name = input("Nafn: ")
            if self.__service.is_valid_name(name) == False:
                print('Rangur insláttur\nSláðu inn eigöngu bókstafi.')
            else:
                break
        while True:
            ssn = input("Kennitala: ")
            errorprompt = self.__service.is_valid_ssn(ssn)
            if not errorprompt:
                break
            else:
                print(errorprompt)
            # if self.__service.is_valid_ssn(ssn) == False:
            #     print('Rangur insláttur\nSláðu inn eingöngu tölustafi.')
            # else:
            #     break
        while True:
            email = input("Netfang: ")
            if self.__service.is_valid_email(email) == False:
                print('Ógilt netfang\nSláðu inn gilt netfang.')
            else:
                break
        while True:
            phoneNr = input("Símanúmer: ")
            if self.__service.is_valid_phoneNr(phoneNr) == False:
                print('Rangur insláttur\nSláðu inn eingöngu tölustafi.')
            else:
                break

        NewCustomer = Customer(name, ssn, email, phoneNr)
        self.__service.add_customer(NewCustomer)

    def get_another_input(self, errorpromt, inputprompt):
        print(errorpromt)
        new_input = input()
        return new_input