from repositories.CarRepository import CarRepository
from models.Car import Car
from ui.AddCarUi import AddCar


class CarService:
    VALID_BRANDS = [Honda, Skoda Civic]
    VALID_GROUP = [1,2,3,4,5,6]
    def __init__(self):
        self.__car_repo = CarRepository()

    def add_car(self, car):
        if self.is_valid_car(car):
            self.__car_repo.add_car(car)

    def is_valid_car(self,car):
        check_doors(Car.get_doors(car)):

        5 < Car.get_doors(car) < 3:

            return False
        if Car.get_brand(car) not in self.VALID_BRANDS:
            return False
        if 7 < Car.get_seats(car) < 2:
            return False 
        if Car.get_transmission(car) != ('b' or 's'):
            return False
        if int(Car.get_group(car)) not in VALID_GROUP:
            return False
        return True

    def check_doors(doors):

        
        