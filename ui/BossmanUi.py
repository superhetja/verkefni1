from services.CarService import CarService
import HeaderUi 

print_header()
ACTION_CHOICES = [1,2,3,4,5,6,7,8,9,10,11,12,13]
class Bossman: 

    def __init__(slef):
        self.__car_service = CarService()

    def main_menu(self):
        while True:
            print((Color.BOLD + "Útleiga"+ Color.END))
            print("1. Skrá nýja útleigu")
            print("2. Fletta upp útleigu")
            print("3. Ská skil")
            print("4. Skoða verðskrá")
            print("5. Uppfæra verð")

            print(Color.BOLD + "Bílar"+ Color.END)
            print("6. Skoða bíla")
            print("7. Skrá nýjan bíl")

            print(Color.BOLD + "Viðskiptavinur"+ Color.END)
            print("8. Skrá nýjan viðskiptavin")
            print("9. Fletta upp viðskiptavini ")
            print("10. Viðskiptavinalisti")

            print(Color.BOLD + "Starfsmaður"+ Color.END)
            print("11. Skrá nýjan starfsmann")
            print("12. Fletta upp starfsmanni")
            print("13. Birta starfsmann")

            action = int(input())

            if action in ACTION_CHOICES:
                break
            else:
                print("Vinsamlegast veldu gildan valmöguleika")
