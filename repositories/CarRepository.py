from models.Car import Car
from repositories.Repository import Repository

class CarRepository(Repository):
    FILELOCATION = 'data/cars.txt'
    MODELCLASS = 'Car'

    def __init__(self):
        Repository.__init__(self)

      