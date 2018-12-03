from car import Car 

class van:
    def __init__(self, price=0):
        self.__price = price()

    def set_price(self):
        '''Endurreiknar verð á Van'''
        return self.__price

    def get_price(self):
        return self.__price.get_price()