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
        inputprompt = 'Tegund: '
        errorprompt = 'Ekki rétt tegund.'
        while True:
            brand = brand.capitalize()
            if brand in self.VALID_BRANDS:
                break
            self.__addcar_ui.get_another_input(errorprompt,inputprompt)

    def check_seats(self,car):
        seats = Car.get_seats(car)
        inputprompt = 'Fjöldi sæta: '
        errorprompt = 'Rangur innsláttur, sláðu inn heiltölu.'
        while True:
            try:
                seats = int(seats)
                if 9 < seats < 2:
                    errorprompt = 'Rangur innsláttur, of mörg sæti'
                    raise ValueError
                break
            except ValueError:
                self.__addcar_ui.get_another_input(errorprompt,inputprompt)

    def check_transmission(self,car):
        transmission = Car.get_transmission(car)
        inputprompt = 'Skipting b/s: '
        errorprompt = 'Rangur innsláttur.'
        while True:
            
        
        