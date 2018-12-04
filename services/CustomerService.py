from repositories.CustomerRepository import CustomerRepository

class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepository()

    def add_customer(self, customer):
        if self.is_valid_customer(customer):
            self.__customer_repo.add_customer(customer)
    
    def is_valid_customer(self, customer):
        name = is_valid_name(get_name(customer))
        email = is_valid_email(get_email(customer))
        ssn = is_valid_ssn(get_ssn(customer))
        phoneNr = is_valid_phoneNr(get_phoneNr(customer))
        return True
    
    def is_valid_name(self, name):    
        if name == str(name):
            return True
        else:
            return False

    def is_valid_email(self, email):
        for char in email:
            if char == '@':
                att = True
            elif char == ".":
                dot = True
            
        if dot == True and att == True:
            return True
        else:
            return False

    def is_valid_ssn(self, ssn):
        if ssn == int(ssn) and len(ssn) == 10:
            return True
        else:
            return False

    def is_valid_phoneNr(self, phoneNr):    
        if phoneNr == int(phoneNr) and len(phoneNr) == 7:
            return True
        else:
            return False

    def get_customers(self):
        return self.__customer_repo.get_customers()