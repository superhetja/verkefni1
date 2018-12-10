from services.CarService import CarService
from HeaderUi import Header
from models.Color import Color
from models.Clear import Clear
from Ui import Ui
from OrderUi import OrderUi
from ShowCarsUi import ShowCars
from ShowCustomerUi import ShowCustomer
from CustomerUi import CustomerUi
from AddCarUi import AddCarUi
from CreateEmployeeUi import CreateEmployee

ACTION_CHOICES = [1,2,3,4,5,6,7,8,9,10,11,12,13]
class Bossman: 

    def __init__(self):
        Ui.__init__(self)
        self.__car_service = CarService()
        self.__header = Header()
        self.__order = OrderUi()
        self.__showcar = ShowCars()
        self.__showcustomer = ShowCustomer()
        self.__customer = CustomerUi()
        self.__addcar = AddCarUi()
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
            #print("13. Birta starfsmann")

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
            elif action == '6':
                self.__showcar.show_cars_menu()
            elif action =='7':
                self.__addcar.add_car_menu()
            elif action == '8':
                self.__customer.new_customer()
            elif action == '9':
                self.__showcustomer.search_customer()
            elif action == '10':
                self.__showcustomer.show_customer_main()
            elif action == '11':
                self.__employee.create_empoyee()
            elif action == '12':
                #Fletta upp starfsmanni
                #self.__
                pass
            # elif action == '13':
            #     #Birta starfsmann
            #     pass