from repositories.OrderRepository import OrderRepository
from models.Order import Order
from repositories.CarRepository import CarRepository
from models.Car import Car
from services.Service import Service


class OrderService(Service):
    REPO = OrderRepository()

    def __init__(self):
        Service.__init__(self)
        self.__car_repo = CarRepository()

    def add_order(self, order): 
        carnumber = order.get_car()
        self.book_car(carnumber)
        self.__repo.add_content(order)

    def book_car(self, carnumber):
        cars = self.__car_repo.get_content()
        for car in cars:
            if car.get_carnumber() == carnumber:
                car.book_car()
                break
        self.__car_repo.overwrite_file(cars)

    # def get_orders(self):
    #     return self.__repo.get_content()

    # def get_matches(self, search):
    #     orders_that_match = []
    #     orders = self.get_orders()
    #     for order in orders:
    #         if search in order.__repr__():
    #             orders_that_match.append(order)
    #         return order
        