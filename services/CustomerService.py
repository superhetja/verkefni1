from repositories.CustomerRepository import CustomerRepository

class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepository()

    def add_customer(self, customer):
        if self.is_valid_customer(customer):
            self.__customer_repo.add_customer(customer)
    
    def is_valid_customer(self, customer):
        name = get_name(customer)
        email = get_email(customer)
        ssn = get_ssn(customer)
        phoneNr = get_phoneNr(customer)
        if name != str(name):
            return False

        for char in email:
            if char == '@':
                att = True
            elif char == ".":
                dot = True
            if dot == True and att == True:
                return True

        if ssn != int(ssn) or len(ssn) != 10:
            return False
        
        if phoneNr != int(phoneNr) or len(phoneNr) != 7:
            return False

    def get_customers(self):
        return self.__customer_repo.get_customers()