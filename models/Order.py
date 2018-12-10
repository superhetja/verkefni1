class Order: 
    def __init__(self, date1, date2, group, car, customer, payment, card_number='',returned = False):
        self.__date1 = date1
        self.__date2 = date2
        self.__car = car
        self.__customer = customer
        self.__payment = payment
        self.__card_number = card_number
        self.__returned = returned

    def __str__(self):
        return "Dagsettning: {} {}, Bíll {}, Viðskiptavinur {}, Greiðslur {}, Kortnúmer {}, Skiladagur {}".format(self.__date1, self.__date2, self.__car, self.__customer, self.__payment, self.__card_number, self.__return)
        
    def __repr__(self):
        return "Order('{}','{}','{}','{}','{}','{}','{}')".format(self.__date1,
        self.__date2,self.__car,self.__customer,self.__payment,self.__card_number,
        self.__returned)

    def get_date1(self):
        return self.__date1
    
    def get_date2(self):
        return self.__date2
    
    def get_time_period(self):
        return (self.__date2 - self.__date1)

    def get_car(self):
        return self.__car

    def get_customer(self):
        return self.__customer

    def get_payment(self):
        return self.__payment

    def get_card_number(self):
        return self.__card_number

    def return_car(self):
        self.__returned = True
        
# if payment == K
# card_number