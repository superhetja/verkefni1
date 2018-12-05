from models.Color import Color
# from models.car import Car
from models.Order import Order
from services.OrderService import OrderRepository

ACTION_CHOICES=[1,2,3,4,5,6,7,8]

class Order():
    def __init__(self):
        self.__service = OrderService
        self.__header = Header()


    def add_order(self):
        while True:
            date1 = input("Sláðu inn úttektardag: ")
            errorpromt = self.__service.is_valid_date1(date1)
                if not errorpromt:
                    break
                else:
                    print(errorpromt)
            date2 = input("Sláðu inn skiladag: ")
            errorpromt = self.__service.is_valid_date2(date2)
            if not errorpromt:
                break
            else:
                print(errorpromt)
       
        while True:        
            group = input("Bílflokkur: ")
            errorpromt = self.__service.is_valid_group(group)
            if not 

        brand = input("Tegund Bíls: ")
        print("Lausir bíla á valdri dagsetningu: ")
        #listi yfir lausa bíla
        user_choice= input("Valinn bíll: ")
        customer= input("Viðskiptavinur: ")
        payment=input("Greiðslumáti(k/kort,p/preningur):")
        if payment == "k":
            card_number=input("Kortanúmer:")
        print("Yfirlit")
        #yfirlit yfir yfirlitið á pöntuninni
        info = input("Eru allar upplýsingar réttar? j/n")
        if info== "j":
            print("Útleiga bókuð")

    def get_another_input(self, errorpromt, inputprompt):
        print(errorpromt)
        new_input = input()
        return new_input
    
    def car_order_menu(self):
            print("Bílflokkar ")
            print("1. Smá bíll ")
            print("2. Lúxus bíll ")
            print("3. Rafbíll ")
            print("4. Jepplingur ")
            print("5. Jeppi ")
            print("6. Sendiferðabíll")
            print("7. Allir flokkar ")
    
    #def print_available_cars(self) 
    #prentar út lausa bíla

#    action = int(input())
#    if action in ACTION_CHOICES:
#        break
#    else:
#        print("Vinsamlegast veldu gildan valmöguleika")
