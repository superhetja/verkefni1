from repositories.CarRepository import CarRepository
from models.Car import Car
from services.Service import Service 

class CarService(Service):
    REPO = CarRepository()

    # def __init__(self):
    #     Service.__init__(self)


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