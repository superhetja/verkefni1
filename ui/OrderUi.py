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

#print("Lausir bíla á valdri dagsetningu: ")
        #listi yfir lausa bíla

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
            payment=input("Greiðslumáti(k/kort,p/preningur):")
            errorprompt = self.__service.is_valis_payment(payment)
            if not errorprompt:
                break
            else:
                print(errorprompt)
            
        if payment == "k": # veit ekki hvað ég geri með þetta

        while True:
            card_number=input("Kortanúmer:")
            errorprompt = self.__service.is_valid_card_number(card_number)
            if not errorprompt:
                break
            else:
                print(errorprompt)
        print("Yfirlit")
        
        #yfirlit yfir yfirlitið á pöntuninni
        while True:
            info = input("Eru allar upplýsingar réttar? j/n")
            errorprompt = self.__service.is_valid_info(info)
            if info == "j":
                print("Útleiga bókuð")
            else:
                print(errorprompt)



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
