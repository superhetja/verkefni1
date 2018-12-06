from services.CarService import CarService
from models.Car import Car
from services.CheckInputService import CheckInput
from models.Clear import Clear
from ui.InputUi import InputUi
class AddCarUi:
    def __init__(self):
        self.__car = CarService()
        self.__check_input = CheckInput()
        self.__clear = Clear()
        self.__input_ui=InputUi()

    def add_car_menu(self):
        self.__clear.clear_screen()
        self.car_group_menu()
        group=self.__input_ui.get_number_between(1,6)

        brand = input('Tegund: ').capitalize()
        subbrand=input('Undirtegund: ').capitalize()
        seats=self.__input_ui.get_number_between(2,7,'Fjöldi sæta: ')
        transmission=self.__input_ui.get_letter('Skipting b/s: ', ['b','s'])
        doors=self.__input_ui.get_number_between(3,5,'Fjöldi dyra: ')

        new_car = Car(group, brand, subbrand, seats, transmission, doors)
        self.__car.add_car(new_car)
        print("Nýskráningu lokið! ")
        self.get_more()

    def get_more(self):
        letter = self.__input_ui.get_letter(self.__input_ui.MOREPROMPT,['j','n'])
        if letter == 'j':
            self.add_car_menu()
        else: #Skipun að fara til baka um eina valmynd
            pass

    def car_group_menu(self):
        print('Bílaflokkar')
        print('1. Smá bíll')
        print('2. Lúxus bíll')
        print('3. Rafbíll')
        print('4. Jepplingur')
        print('5. Jeppi')
        print('6. Sendiferðabíll')


    