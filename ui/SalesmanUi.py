from services.CarService import CarService
from ui.HeaderUi import Header
from models.Clear import Clear
from models.Color import Color
from ui.Ui import Ui
from ui.OrderUi import OrderUi
from ui.ShowCarsUi import ShowCars
from ui.ShowCustomerUi import ShowCustomer
from ui.CustomerUi import CustomerUi
from ui.AddCarUi import AddCarUi
from ui.ShowOrderUi import ShowOrder
from ui.FileDeliveryUi import FileDelivery

class Salesman(Ui):  
    def __init__(self):
        Ui.__init__(self)
        self.__car_service = CarService()
        self.__header = Header()
        self.__order = OrderUi()
        self.__showcar = ShowCars()
        self.__showcustomer = ShowCustomer()
        self.__customer = CustomerUi()
        self.__addcar = AddCarUi()
        self.__showorder = ShowOrder()
        self.__filedelivery = FileDelivery()
        #self.__input_ui = Ui()

    def main_menu(self):
        action = '1'
        while action != '10':
            print(self.__header)
                
            print(Color.BOLD + "Rental"+ Color.END)            
            print("1. Register new rental")
            print("2. Search rental")
            print("3. File delivery")
            print("4. View Price list")

            print(Color.BOLD + "Cars"+ Color.END)
            print("5. View Cars")
            print('6. Register new car')

            print(Color.BOLD + "Customer"+ Color.END)
            print("7. Register new Customer")
            print("8. Search Customer")
            print("9. View Customers")
            print()
            print('10. Quit')

            action = self.get_number_between(1,10)
            if action=='1':
                self.__order.set_order() #Komið
            elif action=='2':
                self.__showorder.show_order_main() #Komið
            elif action=='3':
                self.__filedelivery.file_delivery_main() #Komið
            elif action=='4':
                pass
            elif action =='5':
                self.__showcar.show_cars_menu()
            elif action =='6':
                self.__addcar.add_car_menu()
            elif action == '7':
                self.__customer.customer_main()
            elif action == '8':
                self.__showcustomer.search_customer()
            elif action =='9':
                self.__showcustomer.print_all_customers()