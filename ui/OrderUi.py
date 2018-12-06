from models.Color import Color
from models.Order import Order
from ui.HeaderUi import Header
from services.OrderService import OrderService

ACTION_CHOICES=[1,2,3,4,5,6,7,8]

class OrderUi():
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
        while True:    
            date2 = input("Sláðu inn skiladag: ")
            errorpromt = self.__service.is_valid_date2(date2)
            if not errorpromt:
                break
            else:
                print(errorpromt)
        while True:        
            group = input("Bílflokkur: ")
            errorpromt = self.__service.is_valid_group(group)
            if not errorpromt:
                break
            else:
                print(errorpromt)
        while True:
            brand = input("Tegund Bíls: ")
            errorprompt = self.__service.is_valid_brand(brand)
            if not errorprompt:
                break
            else:
                print(errorprompt)
        #listi yfir lausa bíla
        print("Lausir bíla á valdri dagsetningu: ")
        while True:
            user_choice= input("Valinn bíll: ")
            errorprompt = self.__service.is_valid_user_choice(user_choice)
            if not errorprompt:
                break
            else:
                print(errorprompt)
        while True:
            costomer= input("Viðskiptavinur: ")
            errorprompt = self.__service.is_valid_custumer(custumer)
            if not errorprompt:
                break
            else:
                print(errorprompt)
        while True:
            payment = input("Greiðslumáti(k/kort,p/preningur): ").capitalize()
            errorprompt = self.__service.is_valis_payment(payment)
            if not errorprompt:
                break
            else:
                print(errorprompt)
        if payment == "K":
            while True:
                card_number = input("Kortanúmer: ")
                errorprompt = self.__service.is_valid_card_number(card_number)
                if not errorprompt:
                    break
                else:
                    print(errorprompt)
        #yfirlit yfir yfirlitið á pöntuninni
        print("Yfirlit")
        while True:
            info = input("Eru allar upplýsingar réttar? j/n").capitalize()
            errorprompt = self.__service.is_valid_info(info)
            if info == "J":
                print("Útleiga bókuð")
            else:
                print(errorprompt)
    
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
