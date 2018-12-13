from repositories.OrderRepository import OrderRepository
from models.Order import Order
from repositories.CarRepository import CarRepository
from models.Car import Car
from services.Service import Service
from datetime import date
from models.Price import Price
from services.CarService import CarService


class OrderService(Service):
    REPO = OrderRepository()
    def __init__(self):
        Service.__init__(self)
        self.__order_repo = OrderRepository()
        self.__car_repo = CarRepository()
        self.__car_service = CarService()


    def add_order(self, order):
        '''Tekur inn pöntun og baetir henni við orders.txt'''
        carnumber = order.get_car()
        self.book_car(carnumber)
        self.__content_list.append(order)
        self.__order_repo.add_content(order)

    def book_car(self, carnumber):
        '''Leita að ákveðnu bílnúmeri og skilar inn upplýsingum um hann ef hann er í kerfninu'''
        cars = self.__car_service.__content_list
        for car in cars:
            if car.get_carnumber() == carnumber:
                car.book_car()
                self.__car_repo.overwrite_file(cars)
                break

    def return_car(self, order):
        '''Skilar inn bílnum ef hann finnst í kerfinu'''
        carnumber = order.get_car()
        cars = self.__car_service.__content_list
        for car in cars:
            if car.get_carnumber() == carnumber:
                car.return_car()
                self.__car_repo.overwrite_file(cars)
                break

    def get_datetime(self,day):
        '''Skilar inn dagsetningu'''
        if '.' in day:
            seperator = '.'
        elif '/' in day:
            seperator = '/' 
        elif '-' in day:
            seperator = '-'
        day,month,year = day.split(seperator)
        day = date(int(year), int(month), int(day))
        return day

    def get_time_period(self,date1,date2):
        time_period = (date2 - date1).days
        return time_period

    def get_today(self):
        return date.today()

    def get_extra_insurance(self, choice):
        '''Skilar extra tryggingu ef það er kosið y'''
        if choice == 'y':
            return True
        else:
            return False

    def get_total_insurance(self, extra_insurance):
        '''Skilar inn samlagningu á extra tryggingu og tryggingu'''
        if extra_insurance:
            return Price.EXTRAINSURANCE + Price.INSURANCE
        else:
            return Price.INSURANCE

    def sort_cars(self):
        '''Tekur alla lausa bíla og flokkar þá eftir hvaða flokki þeir tilheyra'''
        available_cars = self.__car_service.get_available_cars()
        car_list = [[],[],[],[],[],[],[]]
        for car in available_cars:
            group = car.get_group()
            car_list[int(group)-1].append(car)
        return car_list, available_cars

    def get_cars_in_group(self, group):
        sorted_list, available_cars = self.sort_cars()
        if group == '7':
            return available_cars
        else:
            return sorted_list[int(group)-1]

    def file_delivery(self, order):
        '''Skilar bílnum og merkir pöntunina sem er skiluð'''
        self.return_car(order)
        orders = self.__content_list
        orders.remove(order)
        order.file_delivery()
        orders.append(order)
        self.__order_repo.overwrite_file(orders)

    def file_delivery_matches(self, search):
        '''Leitar í lista og skilar því'''
        matches = []
        full_list = self.file_delivery_full_content()
        for instance in full_list:
            if (search in instance.__repr__()):
                matches.append(instance)
        return matches

    def file_delivery_full_content(self):
        '''Skilar pöntun'''
        full_list = self.__content_list
        not_returned_orders = []
        for instance in full_list:
            if instance.get_returned() == 'False':
                not_returned_orders.append(instance)
        return not_returned_orders      
        