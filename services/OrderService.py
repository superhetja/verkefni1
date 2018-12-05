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
     #           self.__addorder_ui.get_another_input(errorpromt,inputprompt)

    def check_group(self, order)
        group = group.get_group(group)
        inputprompt = 'Bílaflokkur: '
        errorpromt = 'Rangur innsláttur '
        try:
            group = int(group)
            if 7 < group <1:
                errorpromt = 'Rangur innsláttur!'
                raise ValueError
            return group
        except ValueError:
            pass
     #  self.__addorder_ui.get_another_input(errorpromt,inputprompt)
    

    def check_brand(self, order):
        brand = brand.get_brand(brand)
        inputprompt = 'Tegund: '
        errorprompt = 'Ekki rétt tegund.'
        while True:
            brand = brand.capitalize()
            if brand in self.VALID_BRANDS:
                break
         #   self.__addorder_ui.get_another_input(errorprompt,inputprompt)
    
    def check_user_choice(self, order):
        user_choice = user_choice.get_user_choice(user_choice)
        inputprompt = 'Valinn bíll: '
        errorprompt = 'Rangur innsláttur. '
        while True:
            user_choice = user_choice.capitalize()
            if user_choice in self.VALID_BRANDS:
                break
       # self.__addorder_ui.get_another_input(errorprompt,inputprompt)


    def check_costumer(self, order):
        costumer = costumer.get_costumer(costumer)
        inputprompt = 'Viðskiptavinur: '
        errorprompt = 'Rangur viðskiptavinur! '
        while True:
            if costumer.isalpha():
                return costumer
            else: #self.__addorder_ui.get_another_input(errorprompt,inputprompt)

    def check_payment(self, order):
        payment = payment.get_payment(payment)
        inputprompt = 'Greiðslumáti (k/kort, p/peningur): '
        errorprompt = 'Rangur innsláttur! '
        while True:
            if payment == K():
                return #vantar

    def check_card_number(self, order):
        card_number = card_number.get_card_number(card_number)
        inputprompt = 'Kortanúmer: '
        errorprompt = 'Rangt kortanúmer'
        while True:
            try:
               card_number = int(card_number)
                if 16 < card_number < 1: 
                    errorpromt = 'Rangt kortanúmer reyndu aftur.'
                    raise ValueError
                return card_number
            except ValueError:
                pass
                # self.__addorder_ui.get_another_input(errorprompt, inputprompt)
