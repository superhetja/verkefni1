from Car import Car

class Luxury(Car):
    PRICE_PER_DAY = 8000
    def __init__(self, brand='', days=1, seats=0, transmission='', doors=0):
        Car.__init__(self, brand, days, seats, transmission, doors)
        self.__price = self.PRICE_PER_DAY * days

    def get_price(self):
        return self.__price