from services.CustomerService import CustomerService
from HeaderUi import Color

print_header()
class NewCustomer:
    def __init__(self):
        self.__customer_service = CustomerService()

    def information_about_new_customer(self):
        print(color.BOLD + "Nýskráning viðskiptavina" + color.END)
        print("Upplýsingar um viðskiptavin:")

        name = input("Nafn: ")
        SSN = input("Kennitala: ")
        email = input("Netfang: ")
