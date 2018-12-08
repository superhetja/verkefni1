from models.Color import Color
from models.Order import Order
from ui.HeaderUi import Header
from services.OrderService import OrderService
from ui.InputUi import InputUi
from services.CarService import CarService

class OrderUi:
    def __init__(self):
        self.__service = OrderService()
        self.__header = Header()
        self.__get_input = InputUi()
        self.__car_service = CarService()

    def set_order(self):
        date1 = self.__get_input.get_date(self.__get_input.BOOKINGDATEPROMPT)
        date2 = self.__get_input.get_date(self.__get_input.RETURNDATEPROMPT)
        self.car_group_menu()
        group = self.__get_input.get_number_between(1,7)
        print("Lausir bíla á valdri dagsetningu: ")
        available_cars = self.__car_service.get_available_cars
        self.__get_input.print_list(available_cars)
        car = self.get_car(available_cars)
        customer = self.get_customer()
        payment = self.__get_input.get_letter("Greiðslumáti(k/kort,p/preningur): ", ['k','p'])
        cardnumber = ''
        if payment == 'k':
            cardnumber = self.__get_input.get_number_length(self.__get_input.CARDPROMPT, 8)
        new_order = Order(date1, date2, group, car, customer, payment, cardnumber)
        self.print_order(new_order)
        self.__service.add_order(new_order)
        print("Útleiga bókuð")
    
    def get_customer(self):
        choice = self.__get_input.get_letter('Skrá nýjann eða fletta upp viðskiptavini(s/f):',['s','f'])
        if choice == 'f':
            customer = self.__get_input.get_string('Viðskiptavinur: ')
            customers = ssn
        else:
            pass
        return customer

    def get_car(self, cars):
        car = self.__get_input.get_number_between(1,len(cars))
        return car
        
    def car_group_menu(self):
        print("Bílflokkar")
        print("1. Smá bíll")
        print("2. Lúxus bíll")
        print("3. Rafbíll")
        print("4. Jepplingur")
        print("5. Jeppi")
        print("6. Sendiferðabíll")
        print("7. Allir flokkar ")
    
    def print_order(self, new_order):
        print('Tímabil: {}'.format(new_order.get_time_period()))
        print('Bíll: {}'.format(new_order.get_car()))
        #print('Kostanður: {}'.format(self.__order.get_cost()))
        print('Viðskiptavinur: {}'.format(new_order.get_customer()))
        print('Greiðslumáti: {}'.format(new_order.get_payment()))
        #print('Heildarkostnaður: {}'.format(self.__order.get_full_amount()))
    
    #def print_available_cars(self) 
    #prentar út lausa bíla

#    action = int(input())
#    if action in ACTION_CHOICES:
#        break
#    else:
#        print("Vinsamlegast veldu gildan valmöguleika")