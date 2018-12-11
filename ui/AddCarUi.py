from services.CarService import CarService
from models.Car import Car
from services.CheckInputService import CheckInput
from models.Clear import Clear
from ui.Ui import Ui

class AddCarUi:
    def __init__(self):
        self.__car = CarService()
        self.__check_input = CheckInput()
        self.__clear = Clear()
        self.__input_ui=Ui()

    def add_car_menu(self):
        self.__clear.clear_screen()
        self.car_group_menu()
        group=self.__input_ui.get_number_between(1,6)

        brand = input('Brand: ').capitalize()
        subbrand = input('Subbrand: ').capitalize()
        carnumber = self.__input_ui.get_carnum()
        seats=self.__input_ui.get_number_between(2,7,'Number of seats: ')
        transmission=self.__input_ui.get_letter('Transmission a/s: ', ['a','s'])
        doors=self.__input_ui.get_number_between(3,5,'Number of doors: ')

        new_car = Car(group, brand, subbrand, carnumber,seats, transmission, doors)
        self.__car.add_content(new_car)
        print("Registration complete! ")
        self.get_more()

    def get_more(self):
        letter = self.__input_ui.get_letter(self.__input_ui.MOREPROMPT,['j','n'])
        if letter == 'j':
            self.add_car_menu()
        else: #Skipun að fara til baka um eina valmynd
            pass


    def car_group_menu(self):
        print('Car groups')
        print('1. Standar')
        print('2. Luxury')
        print('3. Electric')
        print('4. Suv')
        print('5. Jeep')
        print('6. Van')