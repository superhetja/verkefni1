from repositories.OrderRepository import OrderRepository
from services.CheckInputService import CheckInput

class OrderService():
    def __init__(self):
        self.__order_repo = OrderRepository()
        self.__check_input = CheckInput()
    
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
        pass

    def is_valid_date(self, date):
        errorprompt = 'Rangur innsláttur\nSláðu inn einungis tölustafi.'
        try:
            date_list = date.split(".")
            for num in date_list:
                date = int(date)
                if 7 < date < 1:
                    errorprompt = 'Ógild dagsetning\nSláðu inn gilda dagsetingu.'
                    raise ValueError
            return None
        except ValueError:
            return errorpromt     
#búið
    def is_valid_group(self, group):
        errorprompt = 'Rangur innsláttur\nSláðu inn gildan hóp'
        try:
            group = int(group)
            if 7 < group <1:
                raise ValueError
            return None
        except ValueError:
            return errorprompt   
#búið
    def is_valid_brand(self, brand):
        pass
        # errorprompt = 'Ekki rétt tegund\nSláðu inn gilda tegund.'
        # brand = brand.capitalize()
        # if brand in self.__check_input:
        #     return None
        # else:
        #     return errorprompt
# BÚið   
    def ia_valid_user_choice(self, user_choice):
        pass
        # errorprompt = 'Rangur innsláttur.'
        # user_choice = user_choice.capitalize()
        # if user_choice in self.ACTION_CHOICES:
        #     return None
        # else:
        #     return errorprompt
    
    def is_valid_custumer(self, custumer):
        #errorprompt = 'Rangur viðskiptavinur'
        for i in custumer:
            if i in custumer:
                if i.isalpha() == False:
                    return False
                else:
                    return True

    def is_valid_payment(self, payment):
        errorprompt = 'Rangur innsláttur\nKort(k)/Peningur(p)'
        if payment == 'K' or payment == 'P':
            return None
        else:
            return errorprompt
#búið
    def is_valid_card_number(self, card_number):
        errorprompt = 'Rangt kortanúmer\nSláðu inn eingöngu tölustafi.'
        try:
            card_number = int(card_number)
            if len(str(card_number)) != 16 : 
                errorprompt = 'Rangt kortanúmer reyndu aftur.'
                raise ValueError
            return None
        except ValueError:
            return errorprompt 
#búið
    def is_valid_info(self, info):
        errorprompt = 'Rangar upplýsingar'
        if info == 'J':
            return None
        else:
            return errorprompt