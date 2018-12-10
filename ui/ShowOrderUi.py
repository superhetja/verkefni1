from models.Order import Order
from models.Color import Color
from ui.Ui import Ui
from services.OrderService import OrderService


class ShowOrder(Ui):

    def __init__(self):
        Ui.__init__(self)
        self.__color = Color()
#        self = InputUi()
        self.__service = OrderService()

    def show_order_main(self):
        '''Aðal fallið'''
        self.print_menu()
        action = self.get_number_between(1,2)
        if action == '1':
            self.search_order()
        else:
            self.print_all_orders()

    def print_menu(self):
        print(Color.BOLD+'Fletta upp pöntun'+Color.END)
        print('1. Fletta upp pöntun')
        print('2. Birta allar pantanir')

    def search_order(self):
        search = input('Sláðu inn leitarsteng:')
        orders = self.__service.get_matches(search)


    def print_all_orders(self):
        orders = self.__service.get_full_content()
        self.print_list(orders)
        if len(orders) == 0:
            self.get_more()
        else:
            self.choice_order(orders)

    def choice_order(self, orders):
        choice = self.get_number_between(1,len(orders)+1)
        chosen_order = orders[int(choice)-1]
        print(chosen_order)
        print('1. Breyta pöntun')
        print('2. Eyða pöntun')
        print('3. Fletta upp annari pöntun')
        print('4. Fata til baka á aðalvalmynd')
        action = self.get_number_between(1,4)
        if action == '1':
            self.__service.remove_instance(chosen_order)


    def get_more(self):
        pass