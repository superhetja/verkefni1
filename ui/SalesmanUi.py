from services.CarService import CarService
from ui.HeaderUi import Header
from models.Clear import Clear
from models.Color import Color
from ui.InputUi import InputUi
from ui.OrderUi import OrderUi
from ui.ShowCarsUi import ShowCars
from ui.ShowCustomerUi import ShowCustomer
from ui.CustomerUi import Customer

class Salesman: 
    def __init__(self):
        self.__car_service = CarService()
        self.__header = Header()
        self.__input_ui = InputUi()
        self.__order = OrderUi()
        self.__showcar = ShowCars()
        self.__showcustomer = ShowCustomer()
        self.__customer = Customer()
        

    def main_menu(self):
        while True:
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
            if action=='1':
                self.__order.set_order()
            elif action=='2':
                pass
            elif action=='3':
                pass
            elif action=='4':
                pass
            elif action =='5':
                self.__showcar.show_cars_menu()
            elif action =='6':
                self.__customer.new_customer()
            elif action =='7':
                self.__showcustomer.show_customer_menu()


            



