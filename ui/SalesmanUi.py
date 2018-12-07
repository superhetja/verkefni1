from services.CarService import CarService
from ui.HeaderUi import Header
from models.Clear import Clear
from models.Color import Color
from ui.InputUi import InputUi

class Salesman: 
    def __init__(self):
        self.__car_service = CarService()
        self.__header = Header()
        self.__input_ui = InputUi()

    def main_menu(self):
        print(self.__header)
            
        print(Color.BOLD + "Útleiga"+ Color.END)            
        print("1. Skrá nýja útleigu")
        print("2. Fletta upp útleigu")
        print("3. Skrá skil")
        print("4. Skoða verðskrá")

        print(Color.BOLD + "Bílar"+ Color.END)
        print("5. Skoða bíla")
        print('6. Skrá nýjann bíl')

        print(Color.BOLD + "Viðskiptavinur"+ Color.END)
        print("6. Skrá nýjan viðskiptavin")
        print("7. Skoða viðskiptavini ")

        action = self.__input_ui.get_number_between(1,7)

