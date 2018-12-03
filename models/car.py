class Car:
    def __init__(self, brand='', price=0, seats=0, transmission='', doors=0):
        self.__brand = brand
        self.__price = price
        self.__seats = seats
        self.__transmission = transmission
        self.__doors = doors

    def __str__(self):
        return "Bíll: {}, Verð: {} kr, Fjöldi dyra: {}, Fjöldi sæta: {}, Skipting: {}".format(self.__brand, self.__price, self.__doors, self.__seats, self.__transmission)

    def get_price(self):
        return self.__price

    def get_brand(self):
        return self.__brand

    def get_seats(self):
        return self.__seats

    def get_transmission(self):
        return self.__transmission

    def get_doors(self):
        return self.__doors