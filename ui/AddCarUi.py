from services.CarService import CarService
from models.Car import Car
from services.CheckInputService import CheckInput
from ui.Ui import Ui


class AddCarUi(Ui):
    def __init__(self):
        Ui.__init__(self)
        self.__car = CarService()
        self.__check_input = CheckInput()
        self.__input_ui=Ui()

    def add_car_menu(self):
        '''prentar ut addcar menu '''
        self.clear_screen()
        self.car_group_menu()
        group=self.__input_ui.get_number_between(1,6)

        brand = input('Brand: ').capitalize()
        subbrand = input('Subbrand: ').capitalize()
        carnumber = self.__input_ui.get_carnum()
        seats=self.__input_ui.get_number_between(2,7,'Number of seats: ')
        transmission=self.get_transmission()
        doors=self.__input_ui.get_number_between(3,5,'Number of doors: ')

        new_car = Car(group, brand, subbrand, carnumber,seats, transmission, doors)
        self.__car.add_content(new_car)
        print("Registration complete! ")
        self.get_more()


    def get_transmission(self):
        '''Biður notanda um skiptinu skilar manual eða auto'''
        print('Transmission:')
        print('1. Automatic')
        print('2. Manual')
        choice = self.get_number_between(1,2)
        if choice == '1':
            return 'Automatic'
        else:
            return 'Manual'

    def get_more(self):
        '''Spyr notenda um meira hvort hann vilji halda afram'''
        letter = self.__input_ui.get_letter(self.__input_ui.MOREPROMPT,['j','n'])
        if letter == 'j':
            self.add_car_menu()
        else: #Skipun að fara til baka um eina valmynd
            pass


    def car_group_menu(self):
        '''menu fyrir bilategurndir'''
        print('Car groups')
        print('1. Standar')
        print('2. Luxury')
        print('3. Electric')
        print('4. Suv')
        print('5. Jeep')
        print('6. Van')