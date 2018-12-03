from services.CarService import CarService
import HeaderUi 

class Salesman: 

    def __init__(slef):
        self.__car_services = CarService()

    def main_menu(self):
        print_header()
        action = True
        while (action == True):
            print("Útleiga")
            print("1. Skrá nýja útleigu")
            print("2. Fletta upp útleigu")
            print("3. Ská skil")
            print("4. Skoða verðskrá")


            print("Bílar")
            print("5. Skoða bíla")

            print("Viðskiptavinur")
            print("7. Skrá nýjan viðskiptavin")
            print("8. Fletta upp viðskiptavini ")
            print("9. Viðskiptavinalisti")

            action = input()


def main():
    man = Salesman()
    print(man)
main()

