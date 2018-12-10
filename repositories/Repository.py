from models.Order import Order
from models.Employee import Employee
from models.Car import Car
from models.Customer import Customer

class Repository:
    FILELOCATION = 'data/customers.txt'
    MODELCLASS = 'Customer'

    def __init__(self):
        self.__repo_list = self.read_file()
   

    def add_content(self, content):
        with open(self.FILELOCATION, 'a+') as aFile:
            aFile.write(content.__repr__() + '\n')
        a_list = self.__repo_list
        a_list.append(content)
        self.__repo_list = a_list
   #   self.__repo_list.append(customer)

    def read_file(self):
        content = []
        with open(self.FILELOCATION) as aFile:
            for line in aFile.readlines():
                instance = eval(line.strip())
                content.append(instance)
            return content

    def get_content(self):
        return self.__repo_list
 
    def overwrite_file(self,new_content):
   #   with open('data/customers.txt,'w'): pass
        with open(self.FILELOCATION, 'w') as aFile:
            for instance in new_content:
                aFile.write(instance.__repr__() + '\n')