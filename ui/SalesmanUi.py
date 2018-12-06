from services.CarService import CarService
from ui.HeaderUi import Header
from models.Clear import Clear
from models.Color import Color
from services.CheckInputService import CheckInput

class Salesman: 
    def __init__(self):
        self.__car_service = CarService()
        self.__header = Header()

    def main_menu(self):
        print(self.__header)
        while True:
            print(Color.BOLD + "Útleiga"+ Color.END)
            print("1. Skrá nýja útleigu")
            print("2. Fletta upp útleigu")
            print("3. Ská skil")
            print("4. Skoða verðskrá")

            print(Color.BOLD + "Bílar"+ Color.END)
            print("5. Skoða bíla")

            print(Color.BOLD + "Viðskiptavinur"+ Color.END)
            print("6. Skrá nýjan viðskiptavin")
            print("7. Fletta upp viðskiptavini ")
            print("8. Viðskiptavinalisti")

            action = int(input())

            if action in ACTION_CHOICES:
                break
            else:
                print("Vinsamlegast veldu gildan valmöguleika")