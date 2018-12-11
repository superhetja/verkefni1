# from models.Car import Car
from ui.Ui import Ui
from services.PriceListService import PriceListService
 
 
class ShowPrice(Ui):
    def __init__(self, STANDARD, LUXURY, ELECTRIC, SMALLSUV, SUV, VAN, TAX, INSURANCE):
        Car.__init__(self)
        self.__service = PriceListServise()
        
 
    def show_price_list(self):
        self.__clear.clear_screen()
        print('Price without insurance (for one day)')
        print('Price for Small car: {}'.format(self.STANDARD))
        print('Price for Luxury car: {}'.format(self.LUXURY))
        print('Price for Electric car: {}'.format(self.ELECTRIC))
        print('Price for SUV: {}'.format(self.SMALLSUV))
        print('Price for Jeep: {}'.format(self.SUV))
        print('Price for Van: {}'.format(self.VAN))

        print('Price with insurance: {}')
        print('Price for Small car: {}'.format(self.__service.calculate_pricelist(self.STANDARD, self.CARSTANDARD))
        print('Price for luxury car: {}'.format(self.__service.calculate_pricelist(self.LUXURY, self.CARLUXURY))
        print('Price for electric car: {}'.format(self.__service.calculate_pricelist(self.ELECTRIC, self.CARELECTRIC))
        print('Price for small suv: {}'.format(self.__service.calculate_pricelist(self.SMALLSUV, self.CARSMALLSUV))
        print('Price for suv: {}'.format(self.__service.calculate_pricelist(self.SUV, self.CARSUV))
        print('Price for van {}'.format(self.__service.calculate_pricelist(self.VAN, self.CARVAN))
        





 
