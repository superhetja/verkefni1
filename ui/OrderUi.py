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
        date1 = self.get_date(self.BOOKINGDATEPROMPT)
        date2 = self.get_date(self.RETURNDATEPROMPT)
        car = self.get_cars()
        customer = self.get_customer()
        payment = self.get_letter("Payment method(c/card,m/money): ", ['c','m'])
        cardnumber = ''
        if payment == 'k':
            cardnumber = self.get_number_length(self.CARDPROMPT, 8)
        new_order = Order(date1, date2, car, customer, payment, cardnumber)
        # self.print_order(new_order)
        self.__service.add_order(new_order)
        print("Car booked")
    
    def get_cars(self):
        cars, total_cars = self.sort_cars()
        self.car_group_menu(cars,total_cars)
        group = self.get_number_between(1,7)
        print("Available cars on the selected date: ")
        self.print_list(cars[int(group)-1])
        car = self.get_car(cars[int(group)-1])
        return car
            
    def sort_cars(self,):
        available_cars = self.__car_service.get_available_cars()
        car_list = [[],[],[],[],[],[],[]]
        for car in available_cars:
            group = car.get_group()
            car_list[int(group)-1].append(car)
        return car_list, len(available_cars)

    def get_customer(self):
        choice = self.get_letter('Register a new customer or look up customer(r/l):',['r','l'])
        if choice == 'l':
            while True:
                search = self.get_string('Enter search string: ')
                customers = self.__customer_service.get_matches(search)
                self.print_list(customers)
                if len(customers) != 0:
                    customber_num = self.get_number_between(1,len(customers))
                    customer = customers[int(customber_num)-1]
                    print('The chosen customer is:', customer)
                    return customer.get_ssn()
        else:
            self.__new_customer.new_customer()
            customers = self.__customer_service.get_full_content()
            customer = customers[-1]
            return customer.get_ssn()

    def get_car(self, cars):
        choice = self.get_number_between(1,len(cars))
        car = cars[len(choice)-1]
        return car.get_carnumber()
        
    def car_group_menu(self,cars,total_cars):
        print("Car group\t\tAvailable cars")
        print("1. Standard car\t\t\t",len(cars[0]))
        print("2. Luxary car\t\t\t",len(cars[1]))
        print("3. electric car\t\t\t",len(cars[2]))
        print("4. SUV\t\t\t\t",len(cars[3]))
        print("5. Jeep\t\t\t\t",len(cars[4]))
        print("6. Van\t\t\t\t",len(cars[5]))
        print("7. All groups\t\t\t",total_cars)
    

    #Búa bara til str fall í Order til að prenta út order
    #Komið en kann ekki að kalla á það
    def print_order(self, new_order):
        print('Tímabil: {} - {}'.format(new_order.get_date1, new_order.get_date2))
        print('Car: {}'.format(new_order.get_car()))
        #print('Heildarkostnaður: {}'.format(self.__order.get_full_amount()))
        print('Customers: {}'.format(new_order.get_customer()))
        print('Payment method: {}'.format(new_order.get_payment()))