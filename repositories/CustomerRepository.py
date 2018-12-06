from models.Customer import Customer

class CustomerRepository:
   def __init__(self):
      pass
   
   def add_customer(self, customer):
      with open('data/customers.txt', 'a+') as aFile:
         aFile.write(Customer.__repr__(customer) + '\n')

   def get_customers(self):
      customers = []
      with open("data/customers.txt") as aFile:
         for line in aFile.readlines():
            customer = eval(line.strip())
            customers.append(customer)
         return customers
