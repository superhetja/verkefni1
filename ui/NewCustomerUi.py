from services.CustomerService import CustomerService
from models.Customer import Customer
from HeaderUi import Color

print_header()
class NewCustomer:
    def __init__(self):
        self.__customer_service = CustomerService()

    def information_about_new_customer(self):
        print(color.BOLD + "Nýskráning viðskiptavina" + color.END)
        print("Upplýsingar um viðskiptavin:")

        name = input("Nafn: ")
        ssn = input("Kennitala: ")
        email = input("Netfang: ")
        phoneNr = input("Símanúmer: ")

        NewCustomer = Customer(name, ssn, email, phoneNr)
        self.__customer_service.add_customer(NewCustomer)
