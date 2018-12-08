from repositories.OrderRepository import OrderRepository
from models.Order import Order
from repositories.CarRepository import CarRepository
from models.Car import Car


class OrderService():
    def __init__(self):
        self.__order_repo = OrderRepository()
        self.__car_repo = CarRepository()

    def add_order(self, order): 
        carnumber = order.get_car()
        self.book_car(carnumber)
        self.__order_repo.add_order(order)

    def book_car(self, carnumber):
        cars = self.__car_repo.get_cars()
        for car in cars:
            if car.get_carnumber() == carnumber:
                car.book_car()
                break
        self.__car_repo.overwrite_file(cars)
        