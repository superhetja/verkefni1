from services.CarService import CarService
from models.Car import Car

class AddCar:

    def __init__(self):
        self.__car_service = CarService()

    def add_car(self):
        self.car_group_menu()
        group = input('Flokkur: ')
        brand = input('Tegund: ').capitalized()
        seats = input('Fjöldi sæta: ')
        transmission = input('Skipting b/s: ').lower()
        doors = input('Fjöldi dyra: ')
        new_car = Car(group, brand, seats, transmission, doors)
        self.__car_service.add_car(new_car)

    def get_another_input(self, errorpromt, inputprompt):
        print(errorpromt)
        new_input = input()
        return new_input

    def car_group_menu(self):
        print('Bílaflokkar')
        print('1. Smá bíll')
        print('2. Lúxus bíll')
        print('3. Rafbíll')
        print('4. Jepplingur')
        print('5. Jeppi')
        print('6. Sendiferðabíll')


    