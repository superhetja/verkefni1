from repositories.CarRepository import CarRepository
from models.Car import Car
from services.Service import Service 

class CarService(Service):
    REPO = CarRepository()

    # def __init__(self):
    #     self.__car_repo = CarRepository()

    # def add_car(self, car):
        #'''Tekur inn bil og sendir hann i repo fyrir bil sem ad baetir honum vid cars.txt'''
    #     self.__car_repo.add_content(car)

    # def get_cars(self):
        #'''Fer inn i repo fyrir bil sem saekir alla bila i cars.txt og skilar theim'''
    #     return self.__car_repo.get_content()

    def get_available_cars(self):
        '''Saekir alla bila sem eru ekki i leigu og skilar theim'''
        available_cars = []
        all_cars = self.get_full_content()
        for car in all_cars:
            if not car.is_booked():
                available_cars.append(car)
        return available_cars

    def get_booked_cars(self):
        '''Saekir alla bila sem eru i leigu og skilar theim'''
        booked_cars = []
        all_cars = self.get_full_content()
        for car in all_cars:
            if car.is_booked():
                booked_cars.append(car)
        return booked_cars