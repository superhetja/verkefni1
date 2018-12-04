from models.Car import Car

class CarRepository:

    def __init__(self):
        pass

    def add_car(self, car):
        with open('./data/cars.txt', 'a+') as aFile:
            aFile.write(Car.__repr__(car)+ '\n')

    def get_cars(self):
        cars = [] 
        with open('data/cars.txt') as aFile:
            for line in aFile.readlines():
                car = eval(line.strip())
                cars.append(car)
            return cars

      