from models.Order import Order
from repositories.Repository import Repository

class OrderRepository(Repository):
    FILELOCATION = './data/orders.txt'
    MODELCLASS = 'Order'
    def __init__(self):
        Repository.__init__(self)

    # def add_order(self, order):
    #     with open('./data/orders.txt', 'a+') as aFile: 
    #         aFile.write(Order.__repr__(order)+'\n')

    # def get_order(self):
    #     orders = []
    #     with open('data/orders.txt') as aFile:
    #         for line in aFile.readlines():
    #             order = eval(line.strip())
    #             orders.append(order)
    #         return orders
