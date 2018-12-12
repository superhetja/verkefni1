from repositories.PriceListRepository import PriceListRepository
from services.Service import Service
from models.Price import Price

class PriceListService(Service):  
    REPO = PriceListRepository()

    def __init__(self):
        self.__price = Price()

    def calculate_price_x_days(self, group, days):
        price_w_tax = self.__price.get_price_one_day(group)
        price_all_period = price_w_tax * int(days)
        return price_all_period
    
    def calculate_price_x_days_w_insurance(self,group,days):
        price_all_period = self.calculate_price_x_days(group,days)
        return price_all_period + self.__price.INSURANCE


    # def calculate_pricelist(self, rent_price_per_day, price_of_car):
    #     #price for one day 
    #     full_price = (rent_price_per_day + (price_of_car * 0.1) / 365 ) * 1.11
    #     return full_price    