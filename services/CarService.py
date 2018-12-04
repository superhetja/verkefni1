from repositories.CarRepository import CarRepository
from models.Car import Car
from ui import AddCarUi
class CarService:
    VAlID_BRANDS  = ['Honda', 'Skoda']
    VALID_GROUP = [1,2,3,4,5,6]
    def __init__(self):
        self.__car_repo = CarRepository()
#        self.__addcar_ui = AddCarUi.AddCarUi()

    def add_car(self, car):
        car = self.get_valid_car(car)
        self.__car_repo.add_car(car)

    def get_valid_car(self,car):
        doors = self.check_doors(car)
        brand = self.check_brand(car)
        seats = self.check_seats(car)
        transmission = self.check_transmission(car)
        group = self.check_group(car)
        valid_car = Car(group,brand,seats,transmission,doors)
        return valid_car
        
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
                return doors
            except ValueError:
                errorprompt = 'Rangur innsláttur/hurðir\nSláðu inn heiltölu.'
#                AddCarUi.AddCarUi.get_another_input(errorprompt,inputprompt)

    def check_brand(self, car):
        brand = Car.get_brand(car)
        inputprompt = 'Tegund: '
        errorprompt = 'Ekki rétt tegund.'
        while True:
            brand = brand.capitalize()
            if brand in self.VAlID_BRANDS:
                return brand
 #           AddCarUi.AddCarUi.get_another_input(errorprompt, inputprompt)

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
                return seats
            except ValueError:
                pass
 #               AddCarUi.AddCarUi.get_another_input(errorprompt,inputprompt)

    def check_transmission(self,car):
        transmission = Car.get_transmission(car)
        inputprompt = 'Skipting b/s: '
        errorprompt = 'Rangur innsláttur.'
        while True:
            transmission = transmission.lower()
            if transmission == 'b' or 's':
                return transmission
    #        AddCarUi.AddCarUi.get_another_input(errorprompt,inputprompt)
            
    def check_group(self, car):
        group = Car.get_group(car)
        inputprompt = 'Flokkur: '
        errorprompt = 'Rangur innsláttur, sláðu inn heiltölu'
        try:
            group = int(group)
            if 7 < group < 1:
                errorprompt = 'Rangur innsláttur.'
                raise ValueError
            return group
        except ValueError:
            pass
    #        AddCarUi.AddCarUi.get_another_input(errorprompt,inputprompt)

        
        