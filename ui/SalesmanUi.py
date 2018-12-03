from services.CarService import CarService
import HeaderUi 

print_header()
ACTION_CHOICES = [1,2,3,4,5,6,7,8]
class Salesman: 
    def __init__(slef):
        self.__car_service = CarService()

    def main_menu(self):
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