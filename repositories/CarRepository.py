from models.Car import Car
class CarRepository:

    def __init__(self):
        pass

    def add_car(self, car):
        with open('./data/cars.txt', 'a+') as aFile:
            aFile.write(Car.__repr__()+ '\n')

    def get_car(self): 
        with open('data/cars.txt') as aFile:
            for line in aFile.readlines():
                Car = eval(line.strip())
                Car.append(Car)
            return Car

      