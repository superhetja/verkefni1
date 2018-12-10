from datetime import date
from models.Price import Price

class Order: 

    def __init__(self, date1, date2, group, car, customer, payment, card_number='',returned = False):
        self.__date1 = date1
        self.__date2 = date2
        self.__car = car
        self.__customer = customer
        self.__payment = payment
        self.__card_number = card_number
        self.__returned = returned
        self.__group = group
        self.__price = self.calculate_price(group)

    def __str__(self):
        return "Dagsetning: {} {}, Bíll {}, Viðskiptavinur {}, Greiðslur {}, Kortnúmer: {}, Staða: {}".format(self.__date1, self.__date2, self.__car, self.__customer, self.__payment, self.__card_number, self.__returned)
        
    def __repr__(self):
        return "Order('{}','{}','{}','{}','{}','{}','{}','{}')".format(self.__date1,
        self.__date2,self.__group,self.__car,self.__customer,self.__payment,self.__card_number,
        self.__returned)

    def get_date1(self):
        return self.__date1
    
    def get_date2(self):
        return self.__date2

    def calculate_price(self, group):
        price_per_day = self.get_price_per_day(group)
        price_all_period = price_per_day * self.get_time_period()
        return price_all_period
    
    def get_time_period(self):
        year1, month1, day1 = self.__date1.split('-')
        year2, month2, day2 = self.__date2.split('-')
        date1 = date(int(year1), int(month1), int(day1))
        date2 = date(int(year2), int(month2), int(day2))
        time_period = (date2 - date1).days
        return time_period

    def get_price_per_day(self, group):
        price_per_day = Price.price_dict[group][Price.PRICE]
        return price_per_day

    def get_group(self,group):
        return Price.price_dict[group][Price.NAME]

    def get_car(self):
        return self.__car

    def get_customer(self):
        return self.__customer

    def get_payment(self):
        return self.__payment

    def get_card_number(self):
        return self.__card_number
    
    def get_price(self):
        return self.__price

    def return_car(self):
        self.__returned = True