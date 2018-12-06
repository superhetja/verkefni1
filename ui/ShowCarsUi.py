from services.CarService import CarService
from services.CheckInputService import CheckInput
from models.Clear import Clear
from ui.InputUi import InputUi

class ShowCars(InputUi):
    def __init__(self):
        self.__service = CarService()
        self.__check_input = CheckInput()
        self.__clear = Clear()

    def show_cars_menu(self):
        self.__clear.clear_screen()
        print('1. Prenta alla bíla.')
        print('2. Prenta lausa bíla.')
        print('3. Prenta bókaða bíla.')

        action = self.get_number_between(1,3)

        if action == '1':
            self.print_all_cars()
        
        if action == '2':
            self.print_available_cars()

        if action == '3':
            self.print_unavailable_cars()

    def print_all_cars(self):
        cars = self.__service.get_cars()
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
        while True:
            action = input('Viltu halda áfram j/n: ').lower()
            errorprompt = self.__check_input.is_valid_letter(action, ['j','n'])
            if errorprompt == None:
                break
            print(errorprompt)
        
        if action == 'j':
            self.show_cars_menu()
        else:
            pass
