from models.Color import Color
from models.Order import Order
from ui.HeaderUi import Header
from services.OrderService import OrderService
from ui.InputUi import InputUi

class OrderUi:
    def __init__(self):
        self.__service = OrderService()
        self.__header = Header()
        self.__get_input = InputUi

    def set_order(self):

        date1 = self.__get_input.get_date(self.__get_input.BOOKINGDATEPROMPT)
        date2 = self.__get_input.get_date(self.__get_input.RETURNDATEPROMPT)
        self.car_group_menu()
        group = self.__get_input.get_number_between(1,7)
        print("Lausir bíla á valdri dagsetningu: ")
        #Prenta út lista yfir alla lausa bíla á valdri dagsetninu
        car = self.__get_input.get_number_between(1,10) #Þarf að laga töluna..
        customer = self.__get_input.get_string('Viðskiptavinur: ')
        payment = self.__get_input.get_letter("Greiðslumáti(k/kort,p/preningur): ", ['k','p'])
        if payment == 'k':
            cardnumber = self.__get_input.get_number_lengt(self.__get_input.CARDPROMPT, 8)
            




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
    
    def car_group_menu(self):
        print("Bílflokkar")
        print("1. Smá bíll")
        print("2. Lúxus bíll")
        print("3. Rafbíll")
        print("4. Jepplingur")
        print("5. Jeppi")
        print("6. Sendiferðabíll")
        print("7. Allir flokkar ")
    
    def print_order(self):
        booking_date=input("Tímabil: ")
        #sækja bíl
        the_cost= input("Kostnaður: ")
        costumer=input("Viðskiptavinur: ")
        ammount= input("Greiðslumáti: ")
        full_ammount= input("Heildarkostnaður: ")
    
    #def print_available_cars(self) 
    #prentar út lausa bíla

#    action = int(input())
#    if action in ACTION_CHOICES:
#        break
#    else:
#        print("Vinsamlegast veldu gildan valmöguleika")