from services.CarService import CarService
from ui.HeaderUi import Header
from models.Color import Color
from models.Clear import Clear
from ui.Ui import Ui
from ui.OrderUi import OrderUi
from ui.ShowCarsUi import ShowCars
from ui.ShowCustomerUi import ShowCustomer
from ui.CustomerUi import CustomerUi
from ui.AddCarUi import AddCarUi
from ui.CreateEmployeeUi import CreateEmployee

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
            print((Color.BOLD + "Rental"+ Color.END))
            print("1. Register new order")
            print("2. Search rental")
            print("3. File delivery")
            print("4. View price list")
            print("5. Update price")

            print(Color.BOLD + "Cars"+ Color.END)
            print("6. View cars")
            print("7. Register new car")

            print(Color.BOLD + "Customer"+ Color.END)
            print("8. Register new customer")
            print("9. Search customer ")
            print("10. View customers")

            print(Color.BOLD + "Employee"+ Color.END)
            print("11. Register new employee")
            print("12. Search employee")
            print('13. View employees')
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