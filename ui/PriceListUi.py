#from models.Car import Car
from models.Price import Price
from ui.Ui import Ui
#from services.PriceListService import PriceListService
 
 
class ShowPrice(Ui):
    def __init__(self):
        #Car.__init__(self)
        #self.__service = PriceListService()
        self.__price = Price()
        
 
    def show_price_list(self):
        #self.__clear.clear_screen()
        print('Price without insurance (for one day)')
        print('Price for Small car: \t\t{:.0f}'.format(self.__price.get_price_one_day('1')))
        print('Price for Luxury car: \t\t{:.0f}'.format(self.__price.get_price_one_day('2')))
        print('Price for Electric car: \t{:.0f}'.format(self.__price.get_price_one_day('3')))
        print('Price for SUV: \t\t\t{:.0f}'.format(self.__price.get_price_one_day('4')))
        print('Price for Jeep: \t\t{:.0f}'.format(self.__price.get_price_one_day('5')))
        print('Price for Van: \t\t\t{:.0f}'.format(self.__price.get_price_one_day('6')))

        # print('Price with insurance: {}')
        # print('Price for Small car: {}'.format(self.__service.calculate_pricelist(self.STANDARD, self.CARSTANDARD)))
        # print('Price for luxury car: {}'.format(self.__service.calculate_pricelist(self.LUXURY, self.CARLUXURY)))
        # print('Price for electric car: {}'.format(self.__service.calculate_pricelist(self.ELECTRIC, self.CARELECTRIC)))
        # print('Price for small suv: {}'.format(self.__service.calculate_pricelist(self.SMALLSUV, self.CARSMALLSUV)))
        # print('Price for suv: {}'.format(self.__service.calculate_pricelist(self.SUV, self.CARSUV)))
        # print('Price for van {}'.format(self.__service.calculate_pricelist(self.VAN, self.CARVAN)))
        





 
