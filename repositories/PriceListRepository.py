from models.Price import Price
from repositories.Repository import Repository


  class PriceListRepository(Repository):
    FILELOCATION = 'data/pricelist.txt'
    MODELCLASS = 'Price'

    
