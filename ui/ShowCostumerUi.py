from services.CostumerService import CostumerService
from services.CheckInputService import CheckInput
from models.costumer import costumer

class ShowCostumer:
    def __init__(self):
        self.__service = CostumerService()
        self.__check_input = CheckInput()
        self.__clear = Clear()

        def show_costumer_menu(self):
            pass
        
        def get_customer(self):
            while True:
                name = input("Nafn: ")
                errorprompt = self.__service.is_valid_name(name)
                if not errorprompt:
                    break
                else:
                    print(errorprompt)
            while True:
                ssn = input("Kennitala: ")
                errorprompt = self.__service.is_valid_ssn(ssn)
                if not errorprompt:
                    break
                else:
                    print(errorprompt)