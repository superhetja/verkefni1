from repositories.CustomerRepository import CustomerRepository
from models.Customer import Customer
from services.Service import Service



class CustomerService(Service):
    REPO = CustomerRepository()

    def __init__(self):
        Service.__init__(self)
        
    def add_customer(self, customer):
        '''Tekur inn vidskiptavin og sendir hann i repo sem baetir honum i customers.txt'''
        self.__repo.add_content(customer)

    def get_full_content(self):
        '''Skilar ollum vidskiptavini i customers.txt'''
        return self.__repo.get_content()

    def get_matches(self, search):
        '''Tekur inn leit og athugar hvort ad leitin passi vid e-h vidskiptavin og skilar theim vidskiptavinum sem passa'''
        customers_who_match = []
        customers = self.get_full_content()
        for customer in customers:
            if search in customer.__repr__():
                customers_who_match.append(customer)
        return customers_who_match
        

    def remove_customer(self, customer):
        '''Tekur inn vidskiptavin og fjarlaegir hann ur cusomers.txt'''
        full_list = self.get_full_content()
        full_list.remove(customer)
        self.__repo.overwrite_file(full_list)
        
    def change_customer(self, to_remove, to_add):
        '''Tekur inn vidskiptavin og fjarlægir hann ur customers.txt og svo breyttan_vidskiptavin og bætir honum við customers.txt'''
        full_list = self.get_full_content()
        full_list.remove(to_remove)
        full_list.append(to_add)
        self.__repo.overwrite_file(full_list)