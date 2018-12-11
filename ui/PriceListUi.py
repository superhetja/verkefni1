# from models.Car import Car
from ui.Ui import Ui
 
 
class ShowPrice(Ui):
    def __init__(self, STANDARD, LUXURY, ELECTRIC, SMALLSUV, SUV, VAN, TAX, INSURANCE):
        Car.__init__(self)
        # self.__STANDARD = STANDARD
        # self.__LUXURY = LUXURY
        # self.__ELECTRIC = ELECTRIC
        # self.__SMALLSUV = SMALLSUV
        # self.__SUV = SUV 
        # self.__VAN = VAN 

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





#     # STANDARD = 5000
#     # LUXURY = 8000
#     # ELECTRIC = 7000
#     # SMALLSUV = 8000
#     # SUV = 10000
#     # VAN = 9000 

#     TAX = 1.11
#     INSURANCE = 30000

 
