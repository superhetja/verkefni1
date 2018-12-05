from repositories.CustomerRepository import CustomerRepository
#from ui.CustomerUi import CustomerUi
from models.Customer import Customer

class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepository()
#        self.__newCustomer_ui = NewCustomer()

    def add_customer(self, customer):
        if self.is_valid_customer(customer):
            self.__customer_repo.add_customer(customer)
    
    def is_valid_customer(self, customer):
        # name = is_valid_name(customer)
        # email = is_valid_email(customer)
        # ssn = is_valid_ssn(customer)
        # phoneNr = is_valid_phoneNr(customer)
        return True
    
    def is_valid_name(self, name):
        name = name.split()
        for i in name:
            if i.isalpha() == False:
                return False
        return True
#                self.__newCustomer_ui.get_another_input(errorpromt, inputprompt)

    def is_valid_email(self, email):
        try:
            atsymbol = email.index('@')
            dot = email.index('.', atsymbol)
            return True
        except ValueError:
            #print(errorprompt)
            return False

    def is_valid_ssn(self, ssn):
        errorprompt = 'Rangur insláttur\nSláðu inn eingöngu tölustafi.'
        try:
            ssn = int(ssn)
            if len(str(ssn)) != 10:
                errorprompt = 'Rangur fjöldi tölustafa'
                raise ValueError
            return None
        except ValueError:
            return errorprompt
#                self.__newCustomer_ui.get_another_input(errorprompt, inputprompt)

    def is_valid_phoneNr(self, phoneNr):
        errorprompt = 'Rangur insláttur\nSláðu inn eingöngu tölustafi.'
        try:
            phoneNr = int(phoneNr)
            if len(str(phoneNr)) != 7:
                errorprompt = 'Rangur fjöldi tölustafa'
                raise ValueError
            return None
        except ValueError:
            return errorprompt
#                self.__newCustomer_ui.get_another_input(errorprompt, inputprompt)

    def get_customers(self):
        return self.__customer_repo.get_customers()