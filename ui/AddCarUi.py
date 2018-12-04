from services.CarService import CarService

class AddCar:

    def __init__(self):
        self.__car_service = CarService()

    def add_car(self):
        self.car_group_menu()
        group = input('Flokkur: ')
        group = self.__car_service.get_groupname(group)
        brand = input('Tegund: ')
        seats = input('Fjöldi sæta: ')
        transmission = input('Skipting b/s: ')
        doors = input('Fjöldi dyra: ')





    def car_group_menu(self):
        print('Bílaflokkar')
        print('1. Smá bíll')
        print('2. Lúxus bíll')
        print('3. Rafbíll')
        print('4. Jepplingur')
        print('5. Jeppi')
        print('6. Sendiferðabíll')


    