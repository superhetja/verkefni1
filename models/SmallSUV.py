from Car import Car

class SmallSUV(Car):
    def __init__(self, price=0):
        self.__price = price

    def set_price(self):
        '''Endurreiknar verð á small SUV'''
        return self.__price

    def get_price(self):
        return self.__price
        

        