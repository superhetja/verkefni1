from services.CarService import CarService
from models.Car import Car
from services.CheckInputService import CheckInput
from models.Clear import Clear

class AddCarUi:
    def __init__(self):
        self.__car = CarService()
        self.__check_input = CheckInput()
        self.__clear = Clear()

    def add_car_menu(self):
        self.__clear.clear_screen()
        self.car_group_menu()
        while True:
            group = input('Flokkur: ')
            errorprompt = self.__check_input.is_valid_number_between(group,1,6)
            if errorprompt == None:
                break
            print(errorprompt)
        brand = input('Tegund: ').capitalize()
        subbrand=input('Undirtegund: ').capitalize()
        while True:
            seats = input('Fjöldi sæta: ')
            errorprompt = self.__check_input.is_valid_number_between(seats,2,7)
            if errorprompt == None:
                break
            print(errorprompt)
        while True:
            transmission = input('Skipting b/s: ')
            errorprompt = self.__check_input.is_valid_letter(transmission, ['b','s'])
            if errorprompt == None:
                break
            print(errorprompt)
        while True:
            doors = input('Fjöldi dyra: ')
            errorprompt = self.__check_input.is_valid_number_between(doors,3,5)
            if errorprompt == None:
                break
            print(errorprompt)
        new_car = Car(group, brand, subbrand, seats, transmission, doors)
        self.__car.add_car(new_car)

    def car_group_menu(self):
        print('Bílaflokkar')
        print('1. Smá bíll')
        print('2. Lúxus bíll')
        print('3. Rafbíll')
        print('4. Jepplingur')
        print('5. Jeppi')
        print('6. Sendiferðabíll')


    