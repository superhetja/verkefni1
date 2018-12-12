#from models.Car import Car
from models.Price import Price
from ui.Ui import Ui
from services.PriceListService import PriceListService
 
 
class ShowPrice(Ui):
    def __init__(self):
        #Car.__init__(self)
        Ui.__init__(self)
        self.__service = PriceListService()
        self.__price = Price()
        
 
    def show_price_list(self):
        '''Main     prentar ut 1 dag'''
        #self.__clear.clear_screen()
        print('Price without insurance for 1 day')
        print('Price for Standard car: \t{:.0f}'.format(self.__price.get_price_one_day('1')))
        print('Price for Luxury car: \t\t{:.0f}'.format(self.__price.get_price_one_day('2')))
        print('Price for Electric car: \t{:.0f}'.format(self.__price.get_price_one_day('3')))
        print('Price for SUV: \t\t\t{:.0f}'.format(self.__price.get_price_one_day('4')))
        print('Price for Jeep: \t\t{:.0f}'.format(self.__price.get_price_one_day('5')))
        print('Price for Van: \t\t\t{:.0f}'.format(self.__price.get_price_one_day('6')))

        print('Price with insurance for 1 day')
        print('Price for Standard car: \t{:.0f}'.format(self.__price.get_price_one_day_w_insurance('1')))
        print('Price for Luxury car: \t\t{:.0f}'.format(self.__price.get_price_one_day_w_insurance('2')))
        print('Price for Electric car: \t{:.0f}'.format(self.__price.get_price_one_day_w_insurance('3')))
        print('Price for Suv: \t\t\t{:.0f}'.format(self.__price.get_price_one_day_w_insurance('4')))
        print('Price for Jeep: \t\t{:.0f}'.format(self.__price.get_price_one_day_w_insurance('5')))
        print('Price for Van \t\t\t{:.0f}'.format(self.__price.get_price_one_day_w_insurance('6')))
        
        self.menu()

    def menu(self):
        '''spyr hversu marga daga vill vidkomandi leigja bilinn '''
        print()
        print('1. Calculate based on days.')
        print('2. Back to Main Menu.')
        action = self.get_number_between(1,2)
        if action == '1':
            self.show_price_list_x_days()
        else:
            pass

    def show_price_list_x_days(self):
        days = self.get_number('How many days: ')
        ''' Pretnar ut utreikinga ut fra notanda inputi '''
        '''Sprentar ut verdlista med og an tryggingu fyrir x marga daga '''
        print('Price without insurance for {} days'.format(days))
        print('Price for Standard car: \t{:.0f}'.format(self.__service.calculate_price_x_days('1',days)))
        print('Price for Luxury car: \t\t{:.0f}'.format(self.__service.calculate_price_x_days('2',days)))
        print('Price for Electric car: \t{:.0f}'.format(self.__service.calculate_price_x_days('3',days)))
        print('Price for SUV: \t\t\t{:.0f}'.format(self.__service.calculate_price_x_days('4',days)))
        print('Price for Jeep: \t\t{:.0f}'.format(self.__service.calculate_price_x_days('5',days)))
        print('Price for Van: \t\t\t{:.0f}'.format(self.__service.calculate_price_x_days('6',days)))
        print()
        print('Price with insurance for {} days'.format(days))
        print('Price for Small car: \t\t{:.0f}'.format(self.__service.calculate_price_x_days_w_insurance('1',days)))
        print('Price for Luxury car: \t\t{:.0f}'.format(self.__service.calculate_price_x_days_w_insurance('2',days)))
        print('Price for Electric car: \t{:.0f}'.format(self.__service.calculate_price_x_days_w_insurance('3',days)))
        print('Price for SUV: \t\t\t{:.0f}'.format(self.__service.calculate_price_x_days_w_insurance('4',days)))
        print('Price for Jeep: \t\t{:.0f}'.format(self.__service.calculate_price_x_days_w_insurance('5',days)))
        print('Price for van \t\t\t{:.0f}'.format(self.__service.calculate_price_x_days_w_insurance('6',days)))
        
        self.menu()