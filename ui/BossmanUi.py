<<<<<<< HEAD
       
class Bossman:
    def __init__():
            pass
        fullname = input('Full nafn: ')
        while True:
            try:
            ssn = int(input(ssn)).strip()
            if len(ssn) == 10:
                break
            else:
                print('Sláðu inn gilt lykilorð!')
            except ValueError:
                print('Sláðu inn eingöngu tölur')
        password = input('Lykilorð: ')
        email = input('Email: ')
        while True:
            admin = input('Admin y/n: ').lower()
            if admin == 'y'
                admin = True
                break
            elif admin == 'n'
                admin = False
                break
            print('Veldu rétt')
=======
from services.CarService import CarService
import HeaderUi 

class Bossman: 

    def __init__(slef):
        self.__car_services = CarService()

    def main_menu(self):
        print_header()
        action = True
        while (action == True):
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

            action = input()
>>>>>>> c7e7b707e2d354e8af6968e90948ecbee72eeaaf
