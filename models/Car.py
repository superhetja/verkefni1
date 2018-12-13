class Car:
    '''Segir til um verðin'''
    PRICE_PER_DAY = 5000
    STANDARD = 5000
    LUXURY = 8000
    ELECTRIC = 7000
    SUV = 8000
    JEEP = 10000
    VAN = 9000
    TAX = 1.11 
    INSURANCE = 30000

    CARSTANDARD = 2,000,000
    CARLUXURY = 8,000,000 
    CARELECTRIC = 4,000,000 
    CARSUV = 3,000,000 
    CARJEEP = 5,000,000 
    CARVAN = 2,000,000 
    
    def __init__(self, group=0, brand='', subbrand='', carnumber=0,seats= 0, transmission='', doors=0, booked=False):
        '''private klasi:flokkur, tegund, undirtegund, bílnúmer,sætafjöldi, skipting, fyrafjöldi, leigan'''
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
        '''Verðin á bílunum '''
        if self.__group == 1:
            price = self.STANDARD
        elif self.__group == 2:
            price = self.LUXURY
        elif self.__group == 3:
            price = self.ELECTRIC
        elif self.__group == 4:
            price = self.SUV
        elif self.__group == 5:
            price = self.JEEP
        elif self.__group == 6:
            price = self.VAN
        return price
        
    def __str__(self):
        return "{:40} \tLicense plate: {} \n\tPrice: {:,d} kr{:12} \t\tNumber of doors: {} \n\tNumber of seats: {:14} \tTransmition: {} \n\tStatus: {}\n".format(self.__brand+' '+self.__subbrand,
        self.__carnumber, self.__price, '',self.__doors, self.__seats, self.__transmission,self.print_status())
    
    def __repr__(self):
        """Prentar"""
        return "Car('{}','{}','{}','{}','{}','{}','{}',{})".format(self.__group,self.__brand,self.__subbrand,self.__carnumber,self.__seats,self.__transmission,self.__doors,self.__booked)
    
    def print_status(self):
        '''Returnar true eða false'''
        if self.__booked == True:
            return 'Not available'
        else:
            return 'Available'

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

    def get_id(self):
        return self.__carnumber