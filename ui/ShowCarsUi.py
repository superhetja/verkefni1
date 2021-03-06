from services.CarService import CarService
from services.CheckInputService import CheckInput
from ui.Ui import Ui
from ui.HeaderUi import Header
from models.Color import Color

class ShowCars(Ui):
    def __init__(self):
        Ui.__init__(self)
        self.__service = CarService()
        self.__check_input = CheckInput()
        self.__header = Header()

    def print_menu(self):
        '''prentar ut valmyndina'''
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
        '''prentar ut alla bilana'''
        cars = self.__service.get_full_content()
        self.print_list(cars)
        self.get_more()

    def print_available_cars(self):
        '''prentar ut lausa bila'''
        cars = self.__service.get_available_cars()
        self.print_list(cars)
        self.get_more()

    def print_unavailable_cars(self):
        '''prentar ut bila sem eru i utleigu'''
        cars = self.__service.get_booked_cars()
        self.print_list(cars)
        self.get_more()

    def get_more(self):
        '''Spyr notenda um meira hvort hann vilji halda afram'''
        letter = self.get_letter(self.MOREPROMPT,['y','n'])
        if letter == 'y':
            self.show_cars_main()
        else: #Skipun að fara til baka um eina valmynd
            pass
