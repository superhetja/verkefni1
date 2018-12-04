from services.CarService import CarService
from models.car import Car

class AddCar:

    def __init__(self):
        self.__car_service = CarService()

    def add_car(self):
        self.car_group_menu()
        group = input('Flokkur: ')
        brand = input('Tegund: ')
        seats = input('Fjöldi sæta: ')
        transmission = input('Skipting b/s: ')
        doors = input('Fjöldi dyra: ')
        new_car = Car(group, brand, seats, transmission, doors)
        self.__car_service.add_car(new_car)


    def car_group_menu(self):
        print('Bílaflokkar')
        print('1. Smá bíll')
        print('2. Lúxus bíll')
        print('3. Rafbíll')
        print('4. Jepplingur')
        print('5. Jeppi')
        print('6. Sendiferðabíll')


    