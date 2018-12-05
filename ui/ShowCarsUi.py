from services.CarService import CarService

class ShowCars:
    def __init__(self):
        self.__service = CarService()

    def print_all_cars(self):
        cars = self.__service.get_cars()
        for car in cars:
            print(car)

    def print_available_cars(self):
        pass
    
    def print_unavailable_cars(self):
        pass

