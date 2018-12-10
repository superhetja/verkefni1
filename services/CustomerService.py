from repositories.CustomerRepository import CustomerRepository
from models.Customer import Customer
from services.Service import Service



class CustomerService(Service):
    REPO = CustomerRepository()

    # def add_customer(self, customer):
    #     self.__repo.add_content(customer)

    # def get_full_content(self):
    #     return self.__repo.get_content()

    # def get_matches(self, search):
    #     customers_who_match = []
    #     customers = self.get_full_content()
    #     for customer in customers:
    #         if search in customer.__repr__():
    #             customers_who_match.append(customer)
    #     return customers_who_match
        

    # def remove_customer(self, customer):
    #     full_list = self.get_full_content()
    #     full_list.remove(customer)
    #     self.__repo.overwrite_file(full_list)
        
    # def change_customer(self, to_remove, to_add):
    #     full_list = self.get_full_content()
    #     full_list.remove(to_remove)
    #     full_list.append(to_add)
    #     self.__repo.overwrite_file(full_list)
