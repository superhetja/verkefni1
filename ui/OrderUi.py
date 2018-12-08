from models.Color import Color
from models.Order import Order
from ui.HeaderUi import Header
from services.OrderService import OrderService
from ui.InputUi import InputUi
from services.CarService import CarService
from services.CustomerService import CustomerService
from models.Customer import Customer
from ui.CustomerUi import CustomerUi
from models.Car import Car

class OrderUi:
    def __init__(self):
        self.__service = OrderService()
        self.__header = Header()
        self.__get_input = InputUi()
        self.__car_service = CarService()
        self.__customer_service = CustomerService()
        self.__new_customer = CustomerUi()

    def set_order(self):
        date1 = self.__get_input.get_date(self.__get_input.BOOKINGDATEPROMPT)
        date2 = self.__get_input.get_date(self.__get_input.RETURNDATEPROMPT)
        car = self.get_cars()
        customer = self.get_customer()
        payment = self.__get_input.get_letter("Greiðslumáti(k/kort,p/preningur): ", ['k','p'])
        cardnumber = ''
        if payment == 'k':
            cardnumber = self.__get_input.get_number_length(self.__get_input.CARDPROMPT, 8)
        new_order = Order(date1, date2, car, customer, payment, cardnumber)
       # self.print_order(new_order)
        self.__service.add_order(new_order)
        print("Útleiga bókuð")
    
    def get_cars(self):
        cars, total_cars = self.sort_cars()
        self.car_group_menu(cars,total_cars)
        group = self.__get_input.get_number_between(1,7)
        print("Lausir bíla á valdri dagsetningu: ")
        self.__get_input.print_list(cars[int(group)-1])
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
        choice = self.__get_input.get_letter('Skrá nýjann eða fletta upp viðskiptavini(s/f):',['s','f'])
        if choice == 'f':
            while True:
                search = self.__get_input.get_string('Sláðu inn leitarstreng: ')
                customers = self.__customer_service.get_matches(search)
                self.__get_input.print_list(customers)
                if len(customers) != 0:
                    customber_num = self.__get_input.get_number_between(1,len(customers))
                    customer = customers[int(customber_num)-1]
                    print('Valinn viðskiptavinur er:', customer)
                    return customer.get_ssn()
        else:
            self.__new_customer.new_customer()
            customers = self.__customer_service.get_customers()
            customer = customers[-1]
            return customer.get_ssn()

    def get_car(self, cars):
        choice = self.__get_input.get_number_between(1,len(cars))
        car = cars[len(choice)-1]
        return car.get_carnumber()
        
    def car_group_menu(self,cars,total_cars):
        print("Bílflokkar\t\tLausir bílar")
        print("1. Smá bíll\t\t\t",len(cars[0]))
        print("2. Lúxus bíll\t\t\t",len(cars[1]))
        print("3. Rafbíll\t\t\t",len(cars[2]))
        print("4. Jepplingur\t\t\t",len(cars[3]))
        print("5. Jeppi\t\t\t",len(cars[4]))
        print("6. Sendiferðabíll\t\t",len(cars[5]))
        print("7. Allir flokkar\t\t",total_cars)
    

    #Búa bara til str fall í Order til að prenta út order
    def print_order(self, new_order):
       # print('Tímabil: {}'.format(new_order.get_time_period()))
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