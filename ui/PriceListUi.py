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
        print('Verð án trygginga (fyrir einn dag)')
        print('Verð fyrir standard bíl: {}'.format(self.STANDARD))
        print('Verð fyrir lúxús bíl: {}'.format(self.LUXURY))
        print('Verð fyrir rafmagns bíl: {}'.format(self.ELECTRIC))
        print('Verð fyrir jeppling: {}'.format(self.SMALLSUV))
        print('Verð fyrir jeppa: {}'.format(self.SUV))
        print('Verð fyrir fluttningabíl: {}'.format(self.VAN))

        print('Verð með tryggingu: {}')





#     # STANDARD = 5000
#     # LUXURY = 8000
#     # ELECTRIC = 7000
#     # SMALLSUV = 8000
#     # SUV = 10000
#     # VAN = 9000 

#     TAX = 1.11
#     INSURANCE = 30000

 
