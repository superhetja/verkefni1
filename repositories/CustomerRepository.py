from models.Customer import Customer

class CustomerRepository:
   def __init__(self):
      pass
   
   def add_customer(self, costumer):
      with open('./data/costumers.txt', 'a+') as aFile:
         aFile.write(Customer.__repr__(costumer) + '\n')

   def get_costumer(self):
      customers = []
      with open("./data/costumers.txt", 'r') as aFile:
         for line in aFile.readLines():
            customer = eval(line.strip())
            customers.append(customer)
         return customers