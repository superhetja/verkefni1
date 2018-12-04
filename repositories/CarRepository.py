from models.Car import car
class CarRepository:

    def __init__(self):
        pass

    def add_car(self, car):
        with open('./data/cars.txt', 'a+') as aFile:
            cars_file.write(Car.__repr__()+ '\n')

    def get_car(self): 
        with open('data/cars.txt') as aFile:
            for line in Car_file.readlines():
                Car = eval(line.strip())
                Car.append(Car)
            return self.__Car

      