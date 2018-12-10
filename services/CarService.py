from repositories.CarRepository import CarRepository
from models.Car import Car
from services.Service import Service 

class CarService(Service):
    REPO = CarRepository()

    # def __init__(self):
    #     self.__car_repo = CarRepository()

    # def add_car(self, car):
    #     self.__car_repo.add_content(car)

    # def get_cars(self):
    #     return self.__car_repo.get_content()

    def get_available_cars(self):
        available_cars = []
        all_cars = self.get_full_content()
        for car in all_cars:
            if not car.is_booked():
                available_cars.append(car)
        return available_cars

    def get_booked_cars(self):
        booked_cars = []
        all_cars = self.get_full_content()
        for car in all_cars:
            if car.is_booked():
                booked_cars.append(car)
        return booked_cars



        
        