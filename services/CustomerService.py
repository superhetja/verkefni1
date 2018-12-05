from repositories.CustomerRepository import CustomerRepository
from ui.NewCustomerUi import NewCustomer
from models.Customer import Customer

class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepository()
#        self.__newCustomer_ui = NewCustomer()

    def add_customer(self, customer):
        if self.is_valid_customer(customer):
            self.__customer_repo.add_customer(customer)
    
    def is_valid_customer(self, customer):
        name = is_valid_name(customer)
        email = is_valid_email(customer)
        ssn = is_valid_ssn(customer)
        phoneNr = is_valid_phoneNr(customer)
        return True
    
    def is_valid_name(self, customer):
        name = Costumer.get_name(costumer)
        inputprompt = 'Nafn: '
        errorprompt = 'Rangur insláttur\nSláðu inn eigöngu bókstafi.'
        while True:
            if name.isalpha():
                return name
            else:
                self.__newCustomer_ui.get_another_input(errorpromt, inputprompt)

    def is_valid_email(self, customer):
        email = Costumer.get_name(customer)
        try:
            atsymbol = email.index('@')
            dot = email.index('.', atsymbol)
            return True
        except ValueError:
            return False

    def is_valid_ssn(self, customer):
        ssn = Costumer.get_name(customer)
        inputprompt = 'Kennitala: '
        while True:
            errorprompt = 'Rangur insláttur\nSláðu inn eingöngu tölustafi.'
            try:
                ssn = int(ssn)
                if ssn != 10:
                    errorprompt = 'Rangur fjöldi tölustafa'
                    raise ValueError
                return ssn
            except ValueError:
                errorprompt = 'Rangur insláttur\nSláðu inn eingöngu tölustafi.'
                self.__newCustomer_ui.get_another_input(errorprompt, inputprompt)

    def is_valid_phoneNr(self, customer):
        phoneNr = Costumer.get_phoneNr(customer)
        inputprompt = 'Símanúmer: '
        while True:
            errorprompt = 'Rangur insláttur\nSláðu inn eingöngu tölustafi.'
            try:
                phoneNr = int(phoneNr)
                if phoneNr != 7:
                    errorprompt = 'Rangur fjöldi tölustafa'
                    raise ValueError
                return phoneNr
            except ValueError:
                errorprompt = 'Rangur insláttur\nSláðu inn eingöngu tölustafi.'
                self.__newCustomer_ui.get_another_input(errorprompt, inputprompt)

    def get_customers(self):
        return self.__customer_repo.get_customers()