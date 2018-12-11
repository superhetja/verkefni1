
from models.Color import Color
from models.Order import Order
from ui.HeaderUi import Header
from services.OrderService import OrderService
from ui.Ui import Ui
from services.CarService import CarService
from services.CustomerService import CustomerService
from models.Customer import Customer
from ui.CustomerUi import CustomerUi
from models.Car import Car
from models.Price import Price

class OrderUi(Ui):
    def __init__(self):
        Ui.__init__(self)
        self.__service = OrderService()
        self.__header = Header()
        #self.__get_input = Ui()
        self.__car_service = CarService()
        self.__customer_service = CustomerService()
        self.__new_customer = CustomerUi()

    def set_order(self):
        date1 = self.get_date(self.BOOKINGDATEPROMPT,)
        date1 = self.__service.get_datetime(date1)
        date2 = self.get_date(self.RETURNDATEPROMPT,)
        date2 = self.__service.get_datetime(date2)
        time_period = self.__service.get_time_period(date1,date2)
        group, car = self.get_group_car()
        self.print_price(group,time_period)
        customer = self.get_customer()
        payment = self.get_letter("Payment method(c/card,m/money): ", ['c','m'])
        cardnumber = ''
        if payment == 'k':
            cardnumber = self.get_number_length(self.CARDPROMPT, 16)
        new_order = Order(str(date1), str(date2), group, car, customer, payment, cardnumber)
       # self.print_order(new_order)
        self.__service.add_order(new_order)
        print("Rented booked")
    

    def print_price(self,group,period):
        tax = Price.TAX
        insurance = Price.INSURANCE
        price = Price.price_dict[group][Price.PRICE]
        total_price = price*period
        print('Price without insurance: ', total_price, 'Price with tax: ',total_price*tax)
        print('Insurance: ', insurance, 'Payment: ',(total_price*tax)+insurance) 

    def get_group_car(self):
        cars, total_cars = self.sort_cars()
        self.car_group_menu(cars,total_cars)
        group = self.get_number_between(1,7)
        print("Available cars on choosen date: ")
        cars_in_group = cars[int(group)-1]
        self.print_list(cars_in_group)
        choice = self.get_number_between(1,len(cars[int(group)-1]))
        car = cars_in_group[int(choice)-1]
        carnum = car.get_carnumber()
        return group, carnum
            
    def sort_cars(self):
        available_cars = self.__car_service.get_available_cars()
        car_list = [[],[],[],[],[],[],[]]
        for car in available_cars:
            group = car.get_group()
            car_list[int(group)-1].append(car)
        return car_list, len(available_cars)

    def get_customer(self):
        choice = self.get_letter('Regester or Look up customer (r/l):',['r','l'])
        if choice == 'f':
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
            return customer.get_ssn()

        
    def car_group_menu(self,cars,total_cars):
        print("Cargroup\t\tAvailable cars")
        print("1. Small car\t\t\t",len(cars[0]))
        print("2. Luxury car\t\t\t",len(cars[1]))
        print("3. Electric car\t\t\t",len(cars[2]))
        print("4. Suv\t\t\t",len(cars[3]))
        print("5. Jeep\t\t\t",len(cars[4]))
        print("6. Van\t\t",len(cars[5]))
        print("7. All groups\t\t",total_cars)
    

    # #Búa bara til str fall í Order til að prenta út order
    # def print_order(self, new_order):
    #     print('Tímabil: {} - {}'.format(new_order.get_date1, new_order.get_date2))
    #     print('Bíll: {}'.format(new_order.get_car))
    #     #print('Kostanður: {}'.format(self.__order.get_cost()))
    #     print('Viðskiptavinur: {}'.format(new_order.get_customer()))
    #     print('Greiðslumáti: {}'.format(new_order.get_payment()))
    #     #print('Heildarkostnaður: {}'.format(new_order.num_of_days * 'PRICE')