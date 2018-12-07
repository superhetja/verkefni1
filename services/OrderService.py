from repositories.OrderRepository import OrderRepository
from services.CheckInputService import CheckInput

class OrderService():
    def __init__(self):
        self.__order_repo = OrderRepository()
        self.__check_input = CheckInput()
    
    def add_order(self, order): 
        self.__order_repo.add_order(order)