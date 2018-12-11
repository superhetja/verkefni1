from services.CarService import CarService
from services.CheckInputService import CheckInput
from models.Clear import Clear
from ui.Ui import Ui
from ui.HeaderUi import Header
from models.Color import Color

class ShowCars:
    def __init__(self):
        Ui.__init__(self)
        self.__service = CarService()
        self.__check_input = CheckInput()
        self.__clear = Clear()
        self.__header = Header()
        #self.__input_ui=Ui()

    def print_menu(self):
        print(Color.BOLD + 'Car menu' + Color.END)
        print('1. Print all cars')
        print('2. Print available cars')
        print('3. Print unavailable cars')

    def show_cars_main(self):
        #eftir .......
        '''Aðal fallið til að byrja klasann'''
        self.clear_screen()
        self.print_menu()
        action = self.get_number_between(1,3)
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
        letter = self.get_letter(self.MOREPROMPT,['j','n'])
        if letter == 'j':
            self.show_cars_menu()
        else: #Skipun að fara til baka um eina valmynd
            pass
