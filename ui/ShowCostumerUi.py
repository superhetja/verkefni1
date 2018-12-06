from services.CostumerService import CostumerService
from services.CheckInputService import CheckInput
from models.costumer import costumer

print_header()
ACTION_CHOICES = [1,2,3,4,5]
#aðgerðir sem notandinn getur notað til þess að velja e-h ákveðinn viðskiptavin

class ShowCostumer:
    def __init__(self):
        self.__service = CostumerService()
        self.__check_input = CheckInput()
        self.__clear = Clear()

        def show_costumer_menu(self):
            user_input=input("Sláðu inn nafn(n) eða kennotölu(k): ").capitalize()
            if user_input=="K":
                user_input_name()
            else:
                user_input_ssn()

        def user_input_name(self):
            pass
        
        def get_customer(self):
            while True:
                name = input("Nafn: ")
                errorprompt = self.__service.is_valid_name(name)
                if not errorprompt:
                    break
                else:
                    print(errorprompt)
        
        def user_input_ssn(self)
            while True:
                ssn = input("Kennitala: ")
                errorprompt= self.__check_input.is__valid_number_lenght(ssn,10)
                errorprompt = self.__service.is_valid_ssn(ssn)
                if not errorprompt:
                    break
                else:
                    print(errorprompt)

        def all_costumers(self)
        pass
        #prenta út alla viðskiptavini með þessu nafni og kt.

        def choice_costumer(self)
        pass
        #choiceCostumer=input("Valinn viðskiptavinur: ")
        #þegar valið er í actions ákveðinn viðskiptavin 
        #yfirlit yfir þessum viðskiptavin

        #Varntar fjöldi leigja og hvort við viljum breyta eða eyða viðskiptavini



        