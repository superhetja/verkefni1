from services.CarService import CarService
from ui.HeaderUi import Header
from models.Color import Color
from ui.Ui import Ui
from ui.OrderUi import OrderUi
from ui.ShowCarsUi import ShowCars
from ui.ShowCustomerUi import ShowCustomer
from ui.CustomerUi import CustomerUi
from ui.AddCarUi import AddCarUi
from ui.ShowOrderUi import ShowOrder
from ui.FileDeliveryUi import FileDelivery
from ui.PriceListUi import ShowPrice

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
        self.__showprice = ShowPrice()

    def main_menu(self):
        '''prentar ut valmynd og hvada numer gerir hvad '''
        action = '1'
        while action != '11':
            self.clear_screen()
            print(self.__header)
                
            print(Color.BOLD + "Order"+ Color.END)            
            print("1. Register new order")
            print("2. Search order")
            print("3. View orders")
            print("4. File delivery")
            print("5. View price list")

            print(Color.BOLD + "Cars"+ Color.END)
            print("6. View cars")
            print('7. Register new car')

            print(Color.BOLD + "Customer"+ Color.END)
            print("8. Register new customer")
            print("9. Search customer")
            print("10. View customers")
            print()
            print('11. Quit')

            action = self.get_number_between(1,11)
            if action=='1':
                self.__order.set_order()
            elif action=='2':
                self.__showorder.show_order_main()
            elif action=='3':
                self.__showorder.print_all_orders()
            elif action == '4':
                self.__filedelivery.file_delivery_main()
            elif action=='5':
                self.__showprice.show_price_list()
            elif action =='6':
                self.__showcar.show_cars_main()
            elif action =='7':
                self.__addcar.add_car_menu()
            elif action == '8':
                self.__customer.customer_main()
            elif action == '9':
                self.__showcustomer.search_customer()
            elif action =='10':
                self.__showcustomer.print_all_customers()