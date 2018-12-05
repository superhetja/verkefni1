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

        return True

    def check_date(self, order)
        date = date.get_date(date)
        inputprompt = 'Sláðu inn úttektardag: '
        while True:
            errorpromt = 'Rangur innsláttur/date\nSláðu inn aftur.'
            try:
                date = int(date)
                if 7 < date < 1:
                    errorpromt = 'Röng dagsetning.'
                    raise ValueError
                break
            except ValueError
                errorpromt = 'Rangur innsláttur/date\nSláðu inn aftur.'
                self.__addorder_ui.get_another_input(errorpromt,inputprompt)

    def check_group(self, order)
        group = group.get_group(group)
        inputprompt = 'Bílaflokkur: '
        errorpromt = 'Rangur bílaflokkur '
        while True:

        #VALNTARRRRR !!!!
        self.__addorder_ui.get_another_input(errorpromt,inputprompt)
    
    def check_brand(self, order):
        brand = Car.get_brand(brand)
        inputprompt = 'Tegund: '
        errorprompt = 'Ekki rétt tegund.'
        while True:
            brand = brand.capitalize()
            if brand in self.VALID_BRANDS:
                break
            self.__addcar_ui.get_another_input(errorprompt,inputprompt)
    
    def check_user_choice(self, order):
        user_choice = user_choice.get_user_choice(user_choice)
        inputprompt = 'Valinn bíll: '
        errorprompt = 'Rangur innsláttur. '
        while True:
            