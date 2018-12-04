form models.Costumer import Costumer
class CustomerRepository:
   def __init__(self):
      pass
   
   def add_costumer(self, costumer):
      with open('./data/costumers.txt', 'a+') as aFile:
         costumers.write(Costumer.__repr__() + '\n')

   def get_costumer(self):
      with open("./data/costumers.txt", 'r') as aFile:
         for line in Costumers.readLines():
            Customer = eval(line.strip())
            Customer.append(Customer)
         return self.__Customer