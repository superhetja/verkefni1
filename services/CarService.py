from repositories.CarRepository import CarRepository
from models.Car import Car
class CarService:


    def __init__(self):
        self.__car_repo = CarRepository()

    def add_car(self, car):
        self.__car_repo.add_car(car)


        
        