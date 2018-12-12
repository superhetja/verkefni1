from models.Order import Order
from models.Car import Car
from models.Customer import Customer
from models.Price import Price

class Repository:
    FILELOCATION = './data/customers.txt'
    MODELCLASS = 'Customer'
    def __init__(self):
        pass

    def add_content(self, content):
        '''bætir vid innihaldid i skra'''
        with open(self.FILELOCATION, 'a+') as aFile:
            aFile.write(content.__repr__() + '\n')
   #   self.__repo_list.append(customer)

    def read_file(self):
        '''les inn file-a'''
        content = []
        with open(self.FILELOCATION) as aFile:
            for line in aFile.readlines():
                instance = eval(line.strip())
                content.append(instance)
            return content
 
    def overwrite_file(self,new_content):
        '''yfirskrifar file-a'''
   #   with open('data/customers.txt,'w'): pass
        with open(self.FILELOCATION, 'w') as aFile:
            for instance in new_content:
                aFile.write(instance.__repr__() + '\n')