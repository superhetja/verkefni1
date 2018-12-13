from ui.Ui import Ui
from services.OrderService import OrderService
from models.Color import Color

class FileDelivery(Ui):
    
    def __init__(self):
        Ui.__init__(self)
        self.__service = OrderService()

    def file_delivery_menu(self):
        '''Prentar ut menu'''
        print(Color.BOLD+'Find order'+Color.END)
        print('1. Search order')
        print('2. View all orders')
    
    def file_delivery_main(self):
        '''Aðal fall! Kallar á menu og bidur notanda um leid'''
        self.clear_screen()
        self.file_delivery_menu()
        action = self.get_number_between(1,2)
        if action == '1':
            self.search_order()
        else:
            self.print_all_orders()
            
    def search_order(self):
        '''Biður um leitarstreng og prentar ut allar pantanir sem passa við þann streng'''
        search = input('Input search: ')
        orders = self.__service.file_delivery_matches(search)
        self.print_list(orders)
        if len(orders) == 0:
            self.search_order()
        else:
            self.choose_order(orders)

    def print_all_orders(self):
        '''Prentar ut allar pantanir'''
        orders = self.__service.file_delivery_full_content()
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
        print('1. File delivery')
        print('2. Choose another order')
        print('3. Back to main menu')
        action = self.get_number_between(1,3)
        if action == '1':
            self.file_delivery(chosen_order)
        elif action == '2':
            self.file_delivery_main()
        else:
            pass
    
    def file_delivery(self, order):
        self.__service.file_delivery(order)
        print('Delivery booked!')
        self.get_more()

    def get_more(self):
        '''Spyr notenda um meira hvort hann vilji halda afram'''
        letter = self.get_letter(self.MOREPROMPT,['y','n'])
        if letter == 'y':
            self.file_delivery_main()
        else:
            pass
