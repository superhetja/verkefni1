from repositories.CustomerRepository import CustomerRepository
from models.Customer import Customer

class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepository()

    def add_customer(self, customer):
        self.__customer_repo.add_customer(customer)


    def get_customers(self):
        return self.__customer_repo.get_customers()

    def get_customer_match(self,searchstr,method):
        customer_who_match= []
        customers = self.get_customers()
        for customer in customers:
          #  method = customer+'.'+method
            if eval(customer.method) == searchstr:
                customer_who_match.append(customer)
        return customer

    def get_matches_name(self, name):
        customer_who_match= []
        customers = self.get_customers()
        for customer in customers:
            if name in customer.get_name():
                customer_who_match.append(customer)
        return customer_who_match

    def get_matches_ssn(self, ssn):
        customer_who_match= []
        customers = self.get_customers()
        for customer in customers:
            if ssn in customer.get_ssn():
                customer_who_match.append(customer)
        return customer_who_match

    def get_matches_phonenr(self, phonenr):
        customer_who_match= []
        customers = self.get_customers()
        for customer in customers:
            if phonenr in customer.get_phoneNr():
                customer_who_match.append(customer)
        return customer_who_match

    def get_matches_email(self, email):
        customer_who_match= []
        customers = self.get_customers()
        for customer in customers:
            if email in customer.get_email():
                customer_who_match.append(customer)
        return customer_who_match