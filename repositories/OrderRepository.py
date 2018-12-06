from models.Order import Order

class OrderRepository: 
    def __init__(self):
        pass

    def add_order(self, order):
        with open('./data/orders.txt', 'a+') as aFile: 
            aFile.write(Order.__repr__(order)+'\n')

    def get_order(self):
        oders = []
        with open('data/orders.txt') as aFile:
            for line in aFile.readlines():
                order = eval(line.strip())
                orders.append(order)
            return orders
