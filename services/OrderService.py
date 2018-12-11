from repositories.OrderRepository import OrderRepository
from models.Order import Order
from repositories.CarRepository import CarRepository
from models.Car import Car
from services.Service import Service
from datetime import date
from models.Price import Price


class OrderService(Service):
    REPO = OrderRepository()

    def __init__(self):
        Service.__init__(self)
        self.__car_repo = CarRepository()
        self.__order_repo = OrderRepository()

    def add_order(self, order): 
        carnumber = order.get_car()
        self.book_car(carnumber)
        self.__order_repo.add_content(order)

    def book_car(self, carnumber):
        cars = self.__car_repo.get_content()
        for car in cars:
            if car.get_carnumber() == carnumber:
                car.book_car()
                break
                self.__car_repo.overwrite_file(cars)
            else:
                s = input('fannst ekki')

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

    # def get_orders(self):
    #     return self.__repo.get_content()

    # def get_matches(self, search):
    #     orders_that_match = []
    #     orders = self.get_orders()
    #     for order in orders:
    #         if search in order.__repr__():
    #             orders_that_match.append(order)
    #         return order
        