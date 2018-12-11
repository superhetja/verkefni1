from models.Order import Order
from models.Color import Color
from ui.Ui import Ui
from services.OrderService import OrderService
from ui.HeaderUi import Header


class ShowOrder(Ui):
    def __init__(self):
        Ui.__init__(self)
        self.__color = Color()
#        self = InputUi()
        self.__service = OrderService()
        self.__header = Header()

    def show_order_main(self):
        '''Aðal fallið'''
        self.print_menu()
        action = self.get_number_between(1,2)
        if action == '1':
            self.search_order()
        else:
            self.print_all_orders()

    def print_menu(self):
        print(Color.BOLD+'Search order'+Color.END)
        print('1.Search order')
        print('2. View all orders')

    def search_order(self):
        search = input('Input search:')
        orders = self.__service.get_matches(search)
        self.print_list(orders)
        if len(orders) == 0:
            self.get_more()
        else:
            pass
            

    def print_all_orders(self):
        orders = self.__service.get_full_content()
        self.print_list(orders)
        if len(orders) == 0:
            self.get_more(self.show_order_main())
        else:
            self.choice_order(orders)

    def choose_order(self, orders):
        choice = self.get_number_between(1,len(orders)+1)
        chosen_order = orders[int(choice)-1]
        print(chosen_order)
        print('1. Delete order')
        print('2. Change order')
        print('3. Search another order')
        print('4. Back to main menu')
        action = self.get_number_between(1,4)
        if action == '1':
            self.__service.remove_instance(chosen_order)
            print('Order deleted')
            self.get_more()
        elif action == '2':
            self.change_order(chosen_order)
        elif action == '3':
            self.search_order()
        else:
            pass

    def change_order(self, order):
        print('What do you want to change?')
        print('1. Pick up date')
        print('2. Return date')
        print('3. Payment methood')
        action = self.get_number_between(1, 4)
        date1 = order.get_date1()
        date2 = order.get_date2()
        group = order.get_group()
        car = order.get_car()
        customer = order.get_customer()
        payment = order.get_payment()
        if action == '1':
            date1 = self.get_date(self.BOOKINGDATEPROMPT)
        elif action == '2':
            date2 = self.get_date(self.RETURNDATEPROMPT)
        elif action == '3':
            payment = self.get_letter("Payment method(c/card,m/money): ", ['c','m'])
            cardnum = ''
            if payment == 'k':
                cardnum = self.get_number_length(self.CARDPROMPT, 8)
        new_order = Order(date1, date2, group, car, customer, payment, cardnum)
        self.__service.change_instance(order, new_order)
        self.__service.add_order(new_order)
        print('Change complete!')
        self.get_more()

    # def get_more(self):
    #     pass