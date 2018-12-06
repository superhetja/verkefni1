from services.CostumerService import CostumerService
from services.CheckInputService import CheckInput
from models.costumer import costumer 

class ShowCostumer:
    def __init__(self):
        self.__service = CostumerService()
        self.__check_input = CheckInput()
        self.__clear = Clear()

        def show_costumer_menu(self):
            