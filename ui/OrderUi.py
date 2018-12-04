import HeaderUi

print_header()
ACTION_CHOICES=[1,2,3,4,5,6,7,8]

class Order():
    def __init__(self):
        self.__order_car=OrderCar()
    
    def order_menu(self):
        while True:
            print("1.Bílflokkar")
    
    def print_available_cars(self) #prentar út lausa bíla
