from models.Car import Car
from repositories.Repository import Repository

class CarRepository(Repository):
    FILELOCATION = 'data/cars.txt'
    MODELCLASS = 'Car'
    # def __init__(self):
    #     self.__car_list = self.read_file()

    # def add_car(self, car):
    #     with open('./data/cars.txt', 'a+') as aFile:
    #         aFile.write(Car.__repr__(car)+ '\n')
    #     a_list = self.__car_list
    #     a_list.append(car)
    #     self.__car_list = a_list

    # def read_file(self):
    #     cars = [] 
    #     with open('data/cars.txt') as aFile:
    #         for line in aFile.readlines():
    #             car = eval(line.strip())
    #             cars.append(car)
    #         return cars

    # def get_cars(self):
    #     return self.__car_list
        
    # def overwrite_file(self,new_content):
    #   with open('data/cars.txt', 'w') as aFile:
    #      for car in new_content:
    #         aFile.write(Car.__repr__(car) + '\n')

      