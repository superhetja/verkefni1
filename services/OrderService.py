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
    #    custumer = is_valid_custumer(order)
    #    payment = is_valid_payment(order)
    #    card_number = is_valid_card_number(order)
        return True
#búið
    def is_valid_date(self, date):
<<<<<<< HEAD
        errorpromt = 'Rangur innsláttur\nSláðu inn aftur.'
        try:
            date = int(date)
            if 7 < date < 1:
                errorpromt = 'Röng dagsetning.'
=======
        errorprompt = 'Rangur innsláttur\nSláðu inn einungis tölustafi.'
        try:
            date = int(date)
            if 7 < date < 1:
                errorprompt = 'Ógild dagsetning dagsetning.'
>>>>>>> b3268b41c8c717e19930ce093ae2d94ac93e4885
                raise ValueError
            return None
        except ValueError:
            return errorprompt     
<<<<<<< HEAD
        #     self.__addorder_ui.get_another_input(errorpromt,inputprompt)

#búið
    def is_valid_group(self, group):
        errorprompt = 'Rangur innsláttur reyndu aftur!'
=======
#búið
    def is_valid_group(self, group):
        errorprompt = 'Ógildur hópur\nSláðu inn tölustaf.'
>>>>>>> b3268b41c8c717e19930ce093ae2d94ac93e4885
        try:
            group = int(group)
            if 7 < group <1:
                errorprompt = 'Sláðu inn gildan hóp.'
                raise ValueError
            return None
        except ValueError:
            return errorprompt   
#búið
    def is_valid_brand(self, brand):
        errorprompt = 'Ekki rétt tegund\nSláðu inn gilda tegund.'
        brand = brand.capitalize()
        if brand in self.VALID_BRANDS:
            return None
        else:
            return errorprompt
<<<<<<< HEAD
         #   self.__addorder_ui.get_another_input(errorprompt,inputprompt)

# vantar eitthvað   
=======
#eftir    
>>>>>>> b3268b41c8c717e19930ce093ae2d94ac93e4885
    def ia_valid_user_choice(self, user_choice):
        errorprompt = 'Rangur innsláttur.'
        try:
            user_choice = user_choice.capitalize()
            if user_choice in self.VALID_BRANDS:
                break
<<<<<<< HEAD
       # self.__addorder_ui.get_another_input(errorprompt,inputprompt)


#búið 
    def is_valid_custumer(self, custumer):
        errorprompt = 'Rangur viðskiptavinur! '
        for i in custumer:
            if i in custumer:
=======
        except ValueError:
            return errorprompt
#búið ????
    def is_valid_costumer(self, costumer):
        errorprompt = 'Rangur viðskiptavinur!'
        for i in costumer:
            if i in costumer:
>>>>>>> b3268b41c8c717e19930ce093ae2d94ac93e4885
                if i.isalpha() == False:
                    return False
                else:
                    return True
#búið 
    def is_valid_payment(self, payment):
        errorprompt = 'Rangur innsláttur'
        if payment == 'K' or payment == 'P':
            return None
        else:
            return errorprompt
#búið
    def is_valid_card_number(self, card_number):
<<<<<<< HEAD
        errorprompt = 'Rangt kortanúmer'
        try:
           card_number = int(card_number)
            if len(str(card_number)) != 16 : 
                errorpromt = 'Rangt kortanúmer reyndu aftur.'
=======
        errorprompt = 'Rangt kortanúmer\Sláðu inn eingöngu tölustafi.'
        try:
            card_number = int(card_number)
            if len(str(card_number)) != 16: 
                errorpromt = 'Of margir tölustafir\nSláðu inn réttan fjölda tölustafa.'
>>>>>>> b3268b41c8c717e19930ce093ae2d94ac93e4885
                raise ValueError
            return None
        except ValueError:
            return errorprompt
<<<<<<< HEAD
                # self.__addorder_ui.get_another_input(errorprompt, inputprompt)
 
#búið ? ? ?
    def is_valid_info(self, info):
        errorprompt = 'Rangar upplýsingar '
        if info == 'j':
            return "Útleiga bókuð"
        else:
            return errorprompt

=======
#búið
    def is_valid_info(self, info):
        errorprompt = 'Rangur insláttur'
        if info == 'J' og info == 'N':
            return None
        else:
            return errorprompt
>>>>>>> b3268b41c8c717e19930ce093ae2d94ac93e4885
