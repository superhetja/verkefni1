from models.Order import Order
from models.Color import Color
from ui.Ui import Ui
from services.OrderService import OrderService
from ui.HeaderUi import Header

#Búin að commenta, og allt komið, efþið breytið passa að það virki!!!
class ShowOrder(Ui):
    def __init__(self): 
        Ui.__init__(self)
        self.__color = Color()
        self.__service = OrderService() 
        self.__header = Header()

    def show_order_main(self):
        '''Aðal fallið'''
        self.clear_screen()
        self.print_menu()
        action = self.get_number_between(1,2)
        if action == '1':
            self.search_order()
        else:
            self.print_all_orders()

    def print_menu(self):
        '''Pretnar ut show order main_menu'''
        print(Color.BOLD+'Search order'+Color.END)
        print('1. Search order')
        print('2. View all orders')

    def search_order(self):
        '''Biður um leitarstreng og prentar ut allar pantanir sem passa við þann streng'''
        search = input('Input search: ')
        orders = self.__service.get_matches(search)
        self.print_list(orders)
        if len(orders) == 0:
            self.get_more()
        else:
            self.choose_order(orders)

    def print_all_orders(self):
        '''Prentar ut allar pantanir'''
        orders = self.__service.get_full_content()
        self.print_list(orders)
        if len(orders) == 0:
            self.get_more()
        else:
            self.choose_order(orders)

    def choose_order(self, orders):
        '''Biður notandann um ad velja order og pretnar svo ut thad sem hann getur gert'''
        choice = self.get_number_between(1,len(orders)+1)
        chosen_order = orders[int(choice)-1]
        print()
        print('Chosen order:')
        print('   ',chosen_order)
        print('1. Delete order')
        print('2. Change order')
        print('3. Search another order')
        print('4. Back to main menu')
        action = self.get_number_between(1,4)
        if action == '1':
            self.__service.return_car(chosen_order)
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
        '''Breytir pontun eftir thvi hvad vidskiptavinur velur'''
        print()
        print(Color.BOLD + 'What do you want to change?' + Color.END)
        print('1. Pick up date')
        print('2. Return date')
        print('3. Payment method')
        print('4. Extra insurance')
        print('5. Nothing')
        action = self.get_number_between(1, 5)
        date1 = order.get_date1()
        date2 = order.get_date2()
        group = order.get_group()
        car = order.get_car()
        extra_insurance = order.get_extra_insurance()
        customer = order.get_customer()
        payment = order.get_payment()
        cardnum = order.get_card_number()
        if action == '1':
            date1 = self.get_date(self.BOOKINGDATEPROMPT)
            date1 = self.__service.get_datetime(date1)
        elif action == '2':
            date2 = self.get_date(self.RETURNDATEPROMPT)
            date2 = self.__service.get_datetime(date2)
        elif action == '3':
            if payment == 'Card':
                payment = 'Cash'
            else:
                payment = 'Card'
        elif action == '4':
            if extra_insurance:
                extra_insurance = False
            else:
                extra_insurance = True
        else:
            self.get_more()
        new_order = Order(str(date1), str(date2), group, car, extra_insurance ,customer, payment, cardnum)
        self.__service.change_instance(order, new_order)
        print('Change complete!')
        self.get_more()

    def get_more(self):
        '''Spyr notenda um meira hvort hann vilji halda afram'''
        letter = self.get_letter(self.MOREPROMPT,['y','n'])
        if letter == 'y':
            self.show_order_main()
        else:
            pass
    # def get_more(self):
    #     pass