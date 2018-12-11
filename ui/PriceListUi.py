#from models.Car import Car
from models.Price import Price
from ui.Ui import Ui
from services.PriceListService import PriceListService
 
 
class ShowPrice(Ui):
    def __init__(self):
        #Car.__init__(self)
        self.__service = PriceListService()
        self.__price = Price()
        
 
    def show_price_list(self,days):
        #self.__clear.clear_screen()
        print('Price without insurance for 1 day')
        print('Price for Small car: \t\t{:.0f}'.format(self.__price.get_price_one_day('1')))
        print('Price for Luxury car: \t\t{:.0f}'.format(self.__price.get_price_one_day('2')))
        print('Price for Electric car: \t{:.0f}'.format(self.__price.get_price_one_day('3')))
        print('Price for SUV: \t\t\t{:.0f}'.format(self.__price.get_price_one_day('4')))
        print('Price for Jeep: \t\t{:.0f}'.format(self.__price.get_price_one_day('5')))
        print('Price for Van: \t\t\t{:.0f}'.format(self.__price.get_price_one_day('6')))

        print('Price with insurance for 1 day')
        print('Price for Small car: {}'.format(self.__price.get_price_one_day_w_insurance('1')))
        print('Price for luxury car: {}'.format(self.__price.get_price_one_day_w_insurance('2')))
        print('Price for electric car: {}'.format(self.__price.get_price_one_day_w_insurance('3')))
        print('Price for small suv: {}'.format(self.__price.get_price_one_day_w_insurance('4')))
        print('Price for suv: {}'.format(self.__price.get_price_one_day_w_insurance('5')))
        print('Price for van {}'.format(self.__price.get_price_one_day_w_insurance('6')))


    def calculate_price_x_days(self):
    	days = self.get_number_between(1,100000,'How many days: ')
        if days = '1':
            self.show_price_list()
        else:
            print('Price without insurance for {} days'.format(days))

        self.show_price_list(days)


        





 
