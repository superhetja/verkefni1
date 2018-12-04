from models.Order import Order
class OrderRepository: 

    def __init__(self):
        pass

    def add_order(self, order):
        with open('./data/orders.txt', 'a+') as aFile: 
            order_file.write(Order.__repr__()+'\n')

    def get_order(self):
        with open('data/cars.txt') as aFile:
            for line in Oder_file.readlines():
                Order = eval(line.strip())
                Order.append(Order)
            return self.__Order
