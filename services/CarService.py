from repositories.CarRepository import CarRepository
from models.Car import Car
from ui.AddCarUi import AddCar


class CarService:
    VALID_BRANDS = [Honda, Skoda Civic]
    VALID_GROUP = [1,2,3,4,5,6]
    def __init__(self):
        self.__car_repo = CarRepository()
        self.__addcar_ui = AddCar()

    def add_car(self, car):
        if self.is_valid_car(car):
            self.__car_repo.add_car(car)

    def is_valid_car(self,car):
        doors = check_doors(car)
        brand = check_brand(car)
        seats = check_seats(car)
        transmission = check_transmission(car)
        group = check_group(car)
        
        if Car.get_brand(car) not in self.VALID_BRANDS:
            return False
        if 7 < Car.get_seats(car) < 2:
            return False 
        if Car.get_transmission(car) != ('b' or 's'):
            return False
        if int(Car.get_group(car)) not in VALID_GROUP:
            return False
        return True

    def check_doors(self, car):
        doors = Car.get_doors(car)
        inputprompt = 'Fjöldi dyra: '
        while True:
            errorprompt = 'Rangur innsláttur/hurðir\nSláðu inn heiltölu.'
            try:
                doors = int(doors)
                if 5 < doors < 3:
                    errorprompt = 'Rangur fjöldi hurða.'
                    raise ValueError
                break
            except ValueError:
                errorprompt = 'Rangur innsláttur/hurðir\nSláðu inn heiltölu.'
                self.__addcar_ui.get_another_input(errorprompt,inputprompt)

    def check_valid(self, car):
        brand = Car.get_brand(car)
        while True
        brand = brand.capitalize()
        if brand 


        
        