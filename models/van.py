from Car import Car 

class van(Car):
    PRICE_PER_DAY = 9000
    def __init__(self, brand='', days=1, seats=0, transmission='', doors=0):
        Car.__init__(self, brand, days, seats, transmission, doors)
        self.__price = self.PRICE_PER_DAY * days


    def get_price(self):
        return self.__price.get_price()

    def Van_print(self):
        Van_print(self)
        print("price: ")

   