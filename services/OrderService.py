from repositories.OrderRepository import OrderRepository

class OrderService(self):
    def __init__(self):
        self.__order_repo = OrderRepository()

    def add_order(self, order): 
        if self.is_valid_order(order):
            self.__order_repo.add_order(order)
    
    def is_valid_order(self, order): 
        date = check_date(order)
        group = check_group(order)
        brand = check_brand(order)
        user_choice = check_user_choice(order)
        costumer = check_costumer(order)
        payment = check_payment(order)
        card_number = check_card_number(order)

    def is_valid_date(self, date)
        if date == int(date) and len (date) == 6:
            return True
        else:
            return False

    def is_valid_group(self, group)
        if group == int(group) 
            return True
        else:
            return False
    
    def is_valid_brand(self, brand)
        if brand == 