
from models.Color import Color
from models.Order import Order
from ui.HeaderUi import Header
from services.OrderService import OrderService
from ui.Ui import Ui
#from services.CarService import CarService
from services.CustomerService import CustomerService
from models.Customer import Customer
from ui.CustomerUi import CustomerUi
from models.Car import Car
from models.Price import Price

#Búin að commenta, og allt komið, efþið breytið passa að það virki!!!
class OrderUi(Ui):
    def __init__(self):
        Ui.__init__(self)
        self.__service = OrderService()
        self.__header = Header()
        self.__customer_service = CustomerService()
        self.__new_customer = CustomerUi()

    def set_order(self):
        '''bokar bil i dag'''
        date1 = self.__service.get_today()
        # date1 = self.get_date(self.BOOKINGDATEPROMPT,)
        # date1 = self.__service.get_datetime(date1)
        date2 = self.get_date(self.RETURNDATEPROMPT, date1)
        date2 = self.__service.get_datetime(date2)
        time_period = self.__service.get_time_period(date1,date2)
        print()
        car = self.get_car()
        carnum = car.get_carnumber()
        group = car.get_group()
        print()
        extra_insurance = self.get_letter('Extra insurance? y/n: ', ['y','n'])
        extra_insurance = self.__service.get_extra_insurance(extra_insurance)
        print()
        self.print_price(group,time_period,extra_insurance)
        print()
        customer = self.get_customer()
        print()
        payment = self.get_payment()
        cardnumber = self.get_number_length(self.CARDPROMPT, 16)
        new_order = Order(str(date1), str(date2), group, carnum, extra_insurance, customer, payment, cardnumber)
       # self.print_order(new_order)
        self.__service.add_order(new_order)
        print()
        print("Rent booked!")
        print()
        self.get_more()
    

    def print_price(self,group,period,extra_insurance):
        '''Pretnar út sundurliðað verð á pöntuninni'''
        tax = Price.TAX
        insurance = self.__service.get_total_insurance(extra_insurance)
        price = Price.price_dict[str(group)][Price.PRICE]
        total_price = price*period
        print('Price of order:')
        print('Price without tax:\t{:,d.0f}\tPrice with tax:\t{:,d.0f}'.format(total_price,total_price*tax))
        print('Insurance: \t\t{:,d.0f}\tPayment: \t{:,d.0f}'.format(insurance,(total_price*tax)+insurance)) 

    def get_car(self):
        '''Skilar bíl sem viskiptavinur velur'''
        sorted_list, all_available_cars = self.__service.sort_cars()
        self.car_group_menu(sorted_list,all_available_cars)
        group = self.get_number_between(1,7)
        print("Available cars on choosen date: ")
        cars_in_group = self.__service.get_cars_in_group(group)
        self.print_list(cars_in_group)
        choice = self.get_number_between(1,len(cars_in_group))
        car = cars_in_group[int(choice)-1]
        print('Choosen car:', car)
        return car

    def get_customer(self):
        '''Flettir upp eða býr til nýjann viðskiptavin skilar kennitölu viðskiptavinar'''
        print('Customer:')
        print('1. Register new customer')
        print('2. Look up existing customer')
        choice = self.get_number_between(1,2)
        if choice == '2':
            while True:
                search = self.get_string('Enter a search string: ')
                customers = self.__customer_service.get_matches(search)
                self.print_list(customers)
                if len(customers) != 0:
                    customber_num = self.get_number_between(1,len(customers))
                    customer = customers[int(customber_num)-1]
                    print('Choosen customer:', customer)
                    return customer.get_ssn()
        else:
            self.__new_customer.new_customer()
            customers = self.__customer_service.get_full_content()
            customer = customers[-1]
            print('Choosen customer:', customer)
            return customer.get_ssn()

    def car_group_menu(self,cars,total_cars):
        '''Prentar út alla bílaflokanna og hversu margir eru lausir'''
        print("Cargroup\t\tAvailable cars")
        print("1. Small car\t\t\t",len(cars[0]))
        print("2. Luxury car\t\t\t",len(cars[1]))
        print("3. Electric car\t\t\t",len(cars[2]))
        print("4. Suv\t\t\t\t",len(cars[3]))
        print("5. Jeep\t\t\t\t",len(cars[4]))
        print("6. Van\t\t\t\t",len(cars[5]))
        print("7. All groups\t\t\t",len(total_cars))

    def get_payment(self):
        '''Bydir notanda um ad velja kort eda pening'''
        print('Payment method:')
        print('1. Card')
        print('2. Cash')
        choice = self.get_number_between(1,2)
        if choice == '1':
            return 'Card'
        else:
            return 'Cash'

    def get_more(self):
        '''Spyr hvort notandi vilji halda afram'''
        letter = self.get_letter(self.MOREPROMPT,['y','n'])
        if letter == 'y':
            self.set_order()
        else:
            pass

    

    # #Búa bara til str fall í Order til að prenta út order
    # def print_order(self, new_order):
    #     print('Tímabil: {} - {}'.format(new_order.get_date1, new_order.get_date2))
    #     print('Bíll: {}'.format(new_order.get_car))
    #     #print('Kostanður: {}'.format(self.__order.get_cost()))
    #     print('Viðskiptavinur: {}'.format(new_order.get_customer()))
    #     print('Greiðslumáti: {}'.format(new_order.get_payment()))
    #     #print('Heildarkostnaður: {}'.format(new_order.num_of_days * 'PRICE')