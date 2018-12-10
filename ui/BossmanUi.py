from services.CarService import CarService
from models.Color import Color
from ShowCustomerUi import ShowCustomer
from HeaderUi import Header
from Ui import Ui
from CreateEmployeeUi import CreateEmployee

ACTION_CHOICES = [1,2,3,4,5,6,7,8,9,10,11,12,13]
class Bossman: 

    def __init__(self):
        Ui.__init__(self)
        self.__car_service = CarService()
        self.__header = Header()
        self.__showcustomer = ShowCustomer()
        self.__employee = CreateEmployee()

    def main_menu(self):
        print(self.__header)
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
            print("10. Skoða viðskiptavini")

            print(Color.BOLD + "Starfsmaður"+ Color.END)
            print("11. Skrá nýjan starfsmann")
            print("12. Fletta upp starfsmanni")
            print("13. Birta starfsmann")

    def action_choice(self):
        while True:
            action = self.get_number_between(1,8)
            if action=='1':
                self.__order.set_order()
            elif action=='2':
                #Fletta upp útleigu
                pass
            elif action=='3':
                #Skrá skil
                pass
            elif action=='4':
                #Skoða verðskrá
                pass
            elif action =='5':
                #Uppfæra verð
                pass
            elif action == '6'
                self.__showcar.show_cars_menu()
            elif action =='7':
                self.__addcar.add_car_menu()
            elif action == '8':
                self.__customer.new_customer()
            elif action == '9':
                self.__showcustomer.serch_customer()
            elif action == '10':
                self.__showcustomer.show_customer_main()
            elif action == '11':
                self.__employee.create_empoyee()
            elif action == '12':
                #self.__
                pass
            elif action == '13':
                


# <<<<<<< HEAD
# class Bossman:
#     def __init__():
#             pass
#         fullname = input('Full nafn: ')
#         while True:
#             try:
#             ssn = int(input(ssn)).strip()
#             if len(ssn) == 10:
#                 break
#             else:
#                 print('Sláðu inn gilt lykilorð!')
#             except ValueError:
#                 print('Sláðu inn eingöngu tölur')
#         password = input('Lykilorð: ')
#         email = input('Email: ')
#         while True:
#             admin = input('Admin y/n: ').lower()
#             if admin == 'y'
#                 admin = True
#                 break
#             elif admin == 'n'
#                 admin = False
#                 break
#             print('Veldu rétt')
# =======
#>>>>>>> 598fea71ae8155241a1bf3939d9423281e8acea5
