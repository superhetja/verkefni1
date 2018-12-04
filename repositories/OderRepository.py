from models.Order import Order
class OrderRepository: 

    def __init__(self):
        pass

    def add_order(self, order):
        with open('./data/orders.txt', 'a+') as aFile: 
            aFile.write(Order.__repr__()+'\n')

    def get_order(self):
        with open('data/cars.txt') as aFile:
            for line in aFile.readlines():
                Order = eval(line.strip())
                Order.append(Order)
            return Order
