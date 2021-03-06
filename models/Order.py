from datetime import date
from models.Price import Price

class Order: 
    '''Klasi fyrir pöntunina'''

    def __init__(self, date1, date2, group, car,extra_insurance, customer, payment, card_number='',returned = False):
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

    def __str__(self):
        '''Prentar út upplýsingar um tíman, bílin, trygginguna og fl.'''
        return "Time period: {} - {} \tCar: {}\n\tExtra Insurance: {} \t\t\tPrice: {:,d} kr \n\tCustomer ssn: {} \t\tPayment: {} \n\tCard number: {} \tStatus: {}\n".format(self.print_date(self.__date1), self.print_date(self.__date2), 
        self.__car, self.print_extra_insurance(),self.__price, self.print_ssn(), self.__payment, self.print_cardnum(), self.get_status())        
    
    def __repr__(self):
        '''Prentar út klasa instans'''
        return "Order('{}','{}','{}','{}',{},'{}','{}','{}',{})".format(self.__date1,
        self.__date2,self.__group,self.__car,self.__extra_insurance,self.__customer,self.__payment,self.__card_number,
        self.__returned)

    def get_status(self):
        if self.__returned == True:
            return 'Delivered'
        else:
            return 'In rent'    #veit ekki með þetta orðalag

    def get_date1(self):
        return self.__date1
    
    def get_date2(self):
        return self.__date2

    def calculate_price(self, group):
        '''Reiknar út hvað það kostar að leigja bíl í einn dag og margfaldar það með tímann sem hann er leigður,skilar útkomunni'''
        price_per_day = self.get_price_per_day(group)
        price_all_period = price_per_day * self.get_time_period()
        return price_all_period
    
    def get_time_period(self):
        '''Mínusar dagsetninguna sem hann er skilaður við dagsetninguna sem hann er lánaður'''
        year1, month1, day1 = self.__date1.split('-')
        year2, month2, day2 = self.__date2.split('-')
        date1 = date(int(year1), int(month1), int(day1))
        date2 = date(int(year2), int(month2), int(day2))
        time_period = (date2 - date1).days
        return time_period

    def print_date(self, date):
        '''Gerir dagsetningu prentanlegri'''
        year, month, day = date.split('-')
        return '{}.{}.{}'.format(day, month, year)

    def print_extra_insurance(self):
        ''' Gerir vidbotatryggingu prentanlega'''
        if self.__extra_insurance == True:
            return 'Yes'
        else:
            return 'No'
    
    def print_ssn(self):
        '''Gerir kennitöluprentanlegri'''
        ssn = self.__customer[:6]+'-'+self.__customer[6:]
        return ssn

    def print_cardnum(self):
        ''' gerir kortanumer prentanlegra'''
        cardnum = self.__card_number[:4]+'-'+self.__card_number[4:8]+'-'+self.__card_number[8:12]+'-'+self.__card_number[12:16]
        return cardnum

    def get_price_per_day(self, group):
        '''Skilar greiðslu á hvað kostar að leigja bíl í einn dag'''
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
        '''Prentar út ef það er búið að skila bílnum '''
        self.__returned = True

    def get_id(self):
        '''Skilar id á pöntunini sem að er bílnúmerið'''
        return self.__car