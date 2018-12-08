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
    def __init__(self, group=0, brand='', subbrand='', carnumber=0,seats= 0, transmission='', doors=0, booked=False):
        self.__group = int(group)
        self.__brand = brand
        self.__subbrand = subbrand
        self.__carnumber = carnumber
        self.__seats = seats
        self.__booked = booked
        self.__transmission = transmission
        self.__doors = doors
        self.__price = self.set_price()
        
    def set_price(self):
        if self.__group == 1:
            price = self.STANDART
        elif self.__group == 2:
            price = self.LUXURY
        elif self.__group == 3:
            price = self.ELECTRIC
        elif self.__group == 4:
            price = self.SMALLSUV
        elif self.__group == 5:
            price = self.SUV
        elif self.__group == 6:
            price = self.VAN
        return price
        
    def __str__(self):
        return "Bíll: {} {}, Bílnúmer: {}, Verð: {} kr, Fjöldi dyra: {}, Fjöldi sæta: {}, Skipting: {}, Í útleigu: {}".format(self.__brand,self.__subbrand,self.__carnumber,self.__price, self.__doors, self.__seats, self.__transmission,self.__booked)
    
    def __repr__(self):
        return "Car('{}','{}','{}','{}','{}','{}','{}',{})".format(self.__group,self.__brand,self.__subbrand,self.__carnumber,self.__seats,self.__transmission,self.__doors,self.__booked)
    
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

    def is_booked(self):
        return self.__booked
    
    def get_carnumber(self):
        return self.__carnumber

    def book_car(self):
        self.__booked = True
    
    def return_car(self):
        self.__booked = False