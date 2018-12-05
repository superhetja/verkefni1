from repositories.OrderRepository import OrderRepository

class OrderService(self):
    def __init__(self):
        self.__order_repo = OrderRepository()
    #   self.__newOrder_ui = NewOrder()
    def add_order(self, order): 
        if self.is_valid_order(order):
            self.__order_repo.add_order(order)
    
    def is_valid_order(self, order): 
    #    date = is_valid_date(order)
    #    group = is_valid_group(order)
    #    brand = is_valid_brand(order)
    #    user_choice = is_valid_user_choice(order)
    #    costumer = is_valid_costumer(order)
    #    payment = is_valid_payment(order)
    #    card_number = is_valid_card_number(order)
        return True

#búið
    def is_valid_date(self, date):
        errorpromt = 'Rangur innsláttur\nSláðu inn aftur.'
            try:
                date = int(date)
                if 7 < date < 1:
                    errorpromt = 'Röng dagsetning.'
                    raise ValueError
                return None
            except ValueError:
                return errorprompt     
        #     self.__addorder_ui.get_another_input(errorpromt,inputprompt)

#búið
    def is_valid_group(self, group)
        try:
            group = int(group)
            if 7 < group <1:
                errorpromt = 'Rangur innsláttur!'
                raise ValueError
            return None
        except ValueError:
            pass
     #  self.__addorder_ui.get_another_input(errorpromt,inputprompt)
    
#búið
    def is_valid_brand(self, brand):
        errorprompt = 'Ekki rétt tegund.'
        brand = brand.capitalize()
        if brand in self.VALID_BRANDS:
            return None
        else:
            return errorprompt
         #   self.__addorder_ui.get_another_input(errorprompt,inputprompt)

#eftir    
    def ia_valid_user_choice(self, user_choice):
        errorprompt = 'Rangur innsláttur. '
        try:
            user_choice = user_choice.capitalize()
            if user_choice in self.VALID_BRANDS:
                break
       # self.__addorder_ui.get_another_input(errorprompt,inputprompt)


#búið ????
    def is_valid_costumer(self, costumer):
        errorprompt = 'Rangur viðskiptavinur! '
        for i in costumer:
            if i in costumer:
                if i.isalpha() == False:
                    return False
                else:
                    return True

#búið 
    def is_valid_payment(self, payment):
        errorprompt = 'Rangur innsláttur! '
        payment.capitalize()
            if payment == K or payment == P:
                return None
            else:
                return errorprompt

#búið
    def is_valid_card_number(self, card_number):
        errorprompt = 'Rangt kortanúmer'
            try:
               card_number = int(card_number)
                if len(str(card_number)) != 16 : 
                    errorpromt = 'Rangt kortanúmer reyndu aftur.'
                    raise ValueError
                return None
            except ValueError:
                return errorprompt
                # self.__addorder_ui.get_another_input(errorprompt, inputprompt)
# vantar info ; #vantar 
    def is_valid_info(self, info):
        errorprompt = 'Rangar upplýsingar '
