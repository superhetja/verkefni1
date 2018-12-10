from models.Customer import Customer
from repositories.Repository import Repository

class CustomerRepository(Repository):
   FILELOCATION = 'data/customers.txt'
   MODELCLASS = 'Customer'
   # def __init__(self):
   #    self.__customer_list = self.read_file()
   
   # def add_customer(self, customer):
   #    with open('data/customers.txt', 'a+') as aFile:
   #       aFile.write(Customer.__repr__(customer) + '\n')
   #    a_list = self.__customer_list
   #    a_list.append(customer)
   #    self.__customer_list = a_list
   # #   self.__customer_list.append(customer)

   # def read_file(self):
   #    customers = []
   #    with open("data/customers.txt") as aFile:
   #       for line in aFile.readlines():
   #          customer = eval(line.strip())
   #          customers.append(customer)
   #       return customers

   # def get_customers(self):
   #    return self.__customer_list
 
   # def overwrite_file(self,new_content):
   # #   with open('data/customers.txt,'w'): pass
   #    with open('data/customers.txt', 'w') as aFile:
   #       for customer in new_content:
   #          aFile.write(Customer.__repr__(customer) + '\n')
