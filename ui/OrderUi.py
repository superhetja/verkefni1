from models.Color import Color
from models.Order import Order
from ui.HeaderUi import Header
from services.OrderService import OrderService
from services.CheckInputService import CheckInput

class OrderUi():
    def __init__(self):
        self.__service = OrderService()
        self.__header = Header()
        self.__check_imput = CheckInput()

    def set_order(self):
        while True:
            date1 = input("Sláðu inn úttektardag: ")
            errorprompt = self.__service.is_valid_date(date1)
            if not errorprompt:
                break
            else:
                print(errorprompt)
        while True:    
            date2 = input("Sláðu inn skiladag: ")
            errorprompt = self.__service.is_valid_date(date2)
            if not errorprompt:
                break
            else:
                print(errorprompt)
        while True:        
            group = input("Bílaflokkur: ")
            errorprompt = self.__service.is_valid_group(group)
            if not errorprompt:
                break
            else:
                print(errorprompt)
        while True:
            brand = input("Tegund Bíls: ")
            errorprompt = self.__service.is_valid_brand(brand)
            if not errorprompt:
                break
            else:
                print(errorprompt)
        print("Lausir bíla á valdri dagsetningu: ")
        #Prenta út lista yfir alla lausa bíla á valdri dagsetninu
        while True:
            user_choice= input("Valinn bíll: ")
            errorprompt = self.__service.is_valid_user_choice(user_choice)
            if not errorprompt:
                break
            else:
                print(errorprompt)
        while True:
            customer= input("Viðskiptavinur: ")
            errorprompt = self.__service.is_valid_customer(customer)
            if not errorprompt:
                break
            else:
                print(errorprompt)
        while True:
            payment = input("Greiðslumáti(k/kort,p/preningur): ").capitalize()
            errorprompt = self.__service.is_valid_payment(payment)
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
        print("Yfirlit")
        #Prenta yfirlit yfir pöntunina
        while True:
            info = input("Eru allar upplýsingar réttar? j/n").capitalize()
            errorprompt = self.__service.is_valid_info(info)
            if info == "J":
                new_order = Order(date1, date2, group, brand, user_choice, customer, payment, card_number)
                self.__service.add_order(new_order)
                print("Útleiga bókuð")
            else:
                print(errorprompt)
    
    def car_order_menu(self):
        print("Bílflokkar")
        print("1. Smá bíll")
        print("2. Lúxus bíll")
        print("3. Rafbíll")
        print("4. Jepplingur")
        print("5. Jeppi")
        print("6. Sendiferðabíll")
        print("7. Allir flokkar ")
    
    #def print_available_cars(self) 
    #prentar út lausa bíla

#    action = int(input())
#    if action in ACTION_CHOICES:
#        break
#    else:
#        print("Vinsamlegast veldu gildan valmöguleika")