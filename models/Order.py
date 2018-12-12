from datetime import date
from models.Price import Price

class Order: 
    """Klasi fyrir pöntunina"""

    def __init__(self, date1, date2, group, car,extra_insurance, customer, payment, card_number='',returned = False):
        """Fall með privit breytum"""
        self.__date1 = date1
        self.__date2 = date2
        self.__car = car
        self.__extra_insurance = extra_insurance
        self.__customer = customer
        self.__payment = payment
        self.__card_number = card_number
        self.__returned = returned
        self.__group = group
        self.__price = self.calculate_price(group)
        self.__group_name = self.get_group_name(group)
        self.__status = self.get_status(returned)

    def __str__(self):
        """Prentar út upplýsingar um tíman, bílin, trygginguna og fl."""
        return "Time period: {} - {} \tCar: {}\n\tExtra Insurance: {} \t\t\tPrice: {} \n\tCustomer: {} \t\t\tPayment: {} \n\tCard number: {} \t\tStatus: {}".format(self.get_printable_date(date1), self.get_printable_date(date2), 
        self.__car, self.__extra_insurance,self.__price, self.__customer, self.__payment, self.__card_number, self.__status)        
    def __repr__(self):
        """Prentar út upplýsingarnar um pöntunina"""
        return "Order('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(self.__date1,
        self.__date2,self.__group,self.__car,self.__extra_insurance,self.__customer,self.__payment,self.__card_number,
        self.__returned)

    def get_status(self, returned):
        if returned == True:
            return 'Delivered'
        else:
            return 'In rent'    #veit ekki með þetta orðalag

    def get_date1(self):
        """Nær í dagsetningu sem bíllinn er leigður"""
        return self.__date1
    
    def get_date2(self):
        """Nær í dagsetninguna sem bíllinn er skilaður"""
        return self.__date2

    def calculate_price(self, group):
        """Reiknar út hvað það kostar að leigja bíl í einn dag 
        og margfaldar það með tímann sem hann er leigður,skilar útkomunni"""
        price_per_day = self.get_price_per_day(group)
        price_all_period = price_per_day * self.get_time_period()
        return price_all_period
    
    def get_time_period(self):
        """Nær í tímann sem bíllinn er leigður með því að setja það í lista, breyta í heiltölu
        og draga dagsetningu 1 við dagsetningu 2. skilar tímanum sem hann er leigður"""
        year1, month1, day1 = self.__date1.split('-')
        year2, month2, day2 = self.__date2.split('-')
        date1 = date(int(year1), int(month1), int(day1))
        date2 = date(int(year2), int(month2), int(day2))
        time_period = (date2 - date1).days
        return time_period

    def get_printable_date(self, date):
        year, month, day = date.split('-')
        return '{}-{}-{}'.format(day, month, year)

    def get_price_per_day(self, group):
        '''Skilar greiðslu á hvað kostar að leiga í einn dag'''
        price_per_day = Price.price_dict[str(group)][Price.PRICE]
        return price_per_day

    def get_group(self):
        return self.__group

    def get_group_name(self,group):
        return Price.price_dict[str(group)][Price.NAME]

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

    def get_extra_insurance(self):
        return self.__extra_insurance

    def get_returned(self):
        return self.__returned

    def file_delivery(self):
        self.__returned = True
        self.__status = 'Delivered'