from services.CarService import CarService
from services.CheckInputService import CheckInput
from models.Clear import Clear
from ui.Ui import Ui

class ShowCars:
    def __init__(self):
        self.__service = CarService()
        self.__check_input = CheckInput()
        self.__clear = Clear()
        self.__input_ui=Ui()

    def show_cars_menu(self):
        self.__clear.clear_screen()
        print('1. Prenta alla bíla.')
        print('2. Prenta lausa bíla.')
        print('3. Prenta bókaða bíla.')

        action = self.__input_ui.get_number_between(1,3)

        if action == '1':
            self.print_all_cars()
        
        if action == '2':
            self.print_available_cars()

        if action == '3':
            self.print_unavailable_cars()

    def print_all_cars(self):
        cars = self.__service.get_full_content()
        for car in cars: 
            print(car)
        self.get_more()

    def print_available_cars(self):
        cars = self.__service.get_available_cars()
        for car in cars:
            print(car)
        self.get_more()

    def print_unavailable_cars(self):
        cars = self.__service.get_booked_cars()
        for car in cars:
            print(car)
        self.get_more()

    def get_more(self):
        letter = self.__input_ui.get_letter(self.__input_ui.MOREPROMPT,['j','n'])
        if letter == 'j':
            self.show_cars_menu()
        else: #Skipun að fara til baka um eina valmynd
            pass
