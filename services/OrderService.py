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
        self.__car_repo = CarRepository()
        self.__order_repo = OrderRepository()
        self.__car_service = CarService()

    def add_order(self, order): 
        carnumber = order.get_car()
        self.book_car(carnumber)
        self.__order_repo.add_content(order)

    def book_car(self, carnumber):
        cars = self.__car_repo.get_content()
        for car in cars:
            if car.get_carnumber() == carnumber:
                car.book_car()
                self.__car_repo.overwrite_file(cars)
                break

    def return_car(self, order):
        carnumber = order.get_car()
        cars = self.__car_repo.get_content()
        for car in cars:
            if car.get_carnumber() == carnumber:
                car.return_car()
                self.__car_repo.overwrite_file(cars)
                break

    def get_datetime(self,day):
        day, month, year = day.split('.')
        day = date(int(year), int(month), int(day))
        return day

    def get_time_period(self,date1,date2):
        time_period = (date2 - date1).days
        return time_period

    def get_today(self):
        return date.today()

    def get_extra_insurance(self, choice):
        if choice == 'y':
            return True
        else:
            return False

    def get_total_insurance(self, extra_insurance):
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
        self.return_car(order)
        orders = self.get_full_content()
        orders.remove(order)
        order.file_delivery()
        orders.append(order)
        self.__order_repo.overwrite_file(orders)
        

        