from repositories.PriceListRepository import PriceListRepository
from services.Service import Service

class PriceListService(service):  
REPO = PriceListRepository()


def __init__(self):
    self.__pricelist_repo = PriceListRepository()

def calculate_pricelist(self, rent_price_per_day, price_of_car):
    #price for one day 
    full_price = (rent_price_per_day + (price_of_car * 0.1) / 365 ) * 1.11
    









    