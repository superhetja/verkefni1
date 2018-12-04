class Car:
    PRICE_PER_DAY = 5000
    STANDART = 5000
    LUXURY = 8000
    ELECTRIC = 7000
    SMALLSUV = 8000
    SUV = 10000
    VAN = 9000
    TAX = 1.11
    INSURANCE = 30000
    def __init__(self, group=0, brand='', seats=0, transmission='', doors=0):
        self.__group = int(group)
        self.__brand = brand
        self.__seats = seats
        self.__transmission = transmission
        self.__doors = doors
        
    def set_price(self):
        self.__price = 0
        if self.__group == 1:
            self.__price == self.STANDART
        elif self.__group == 2:
            self.__price == self.LUXURY
        elif self.__group == 3:
            self.__price == self.ELECTRIC
        elif self.__group == 4:
            self.__price == self.SMALLSUV
        elif self.__group == 5:
            self.__price == self.SUV
        elif self.__group == 6:
            self.__price == self.VAN
        
    def __str__(self):
        return "Bíll: {}, Verð: {} kr, Fjöldi dyra: {}, Fjöldi sæta: {}, Skipting: {}".format(self.__brand, self.__price, self.__doors, self.__seats, self.__transmission)
    
    def __repr__(self):
        return "Car('{}','{}','{}','{}','{}')".format(self.__group,self.__brand,self.__seats,self.__transmission,self.__doors)
    
    def get_price(self):
        self.set_price()
        return self.__price

    def get_brand(self):
        return self.__brand

    def get_seats(self):
        return self.__seats

    def get_transmission(self):
        return self.__transmission

    def get_doors(self):
        return self.__doors

    def get_group(self):
        return self.__group