from services.CarService import CarService
from models.Car import Car

class AddCarUi:

    def __init__(self):
        self.__service = CarService()

    def add_car_menu(self):
        self.car_group_menu()
        group = input('Flokkur: ')
        brand = input('Tegund: ')
        seats = input('Fjöldi sæta: ')
        transmission = input('Skipting b/s: ').lower()
        doors = input('Fjöldi dyra: ')
        new_car = Car(group, brand, seats, transmission, doors)
        self.__service.add_car(new_car)

    def get_input(self, errorpromt, inputprompt):
        print(errorpromt)
        new_input = input()
        return new_input

    def prompt_error(self, errorpromt):
        print(errorpromt)

    def car_group_menu(self):
        print('Bílaflokkar')
        print('1. Smá bíll')
        print('2. Lúxus bíll')
        print('3. Rafbíll')
        print('4. Jepplingur')
        print('5. Jeppi')
        print('6. Sendiferðabíll')


    