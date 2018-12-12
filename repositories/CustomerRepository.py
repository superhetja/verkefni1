from models.Customer import Customer
from repositories.Repository import Repository

class CustomerRepository(Repository):
   FILELOCATION = 'data/customers.txt'
   MODELCLASS = 'Customer'
   def __init__(self):
      Repository.__init__(self)