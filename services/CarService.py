from repositories.CarRepository import CarRepository
from models.Car import Car
#from ui import AddCarUi
class CarService:
    VAlID_BRANDS = ["Suzuki","Honda", "Hyundai","Toyota", "Volkswagen","Lexus","Renault",
    "Mazda","Kia","Opel","Ford","Skoda","Mercedez Benz","Nissan","Jeep","Land Rover",+
    "Mitsubishi","Volvo","Citroen","VW","Audi","BMW","Chevrolet","Mini"]
    VALID_GROUP = [1,2,3,4,5,6]
    def __init__(self):
        self.__car_repo = CarRepository()
#        self.__addcar_ui = AddCarUi.AddCarUi()

    def add_car(self, car):
        car = self.get_valid_car(car)
        self.__car_repo.add_car(car)

    def get_valid_car(self,car):
        doors = self.get_doors(car)
        brand = self.get_brand(car)
        seats = self.get_seats(car)
        transmission = self.get_transmission(car)
        group = self.get_group(car)
        valid_car = Car(group,brand,seats,transmission,doors)
        return valid_car
        
    def is_valid_doors(self, car):
        doors = Car.get_doors(car)
        inputprompt = 'Fjöldi dyra: '
        while True:
            errorprompt = 'Rangur innsláttur/hurðir\nSláðu inn heiltölu.'
            try:
                doors = int(doors)
                if 5 < doors < 3:
                    errorprompt = 'Rangur fjöldi hurða.'
                    raise ValueError
                return doors
            except ValueError:
                errorprompt = 'Rangur innsláttur/hurðir\nSláðu inn heiltölu.'
#                AddCarUi.AddCarUi.get_input(errorprompt,inputprompt)

    def is_valid_brand(self, brand):
        inputprompt = 'Tegund: '
        errorprompt = 'Ekki rétt tegund.'
        while True:
            brand = brand.capitalize()
            if brand in self.VAlID_BRANDS:
                return brand
 #           AddCarUi.AddCarUi.get_input(errorprompt, inputprompt)
    def is_valid_subbrand(self,subbrand):
        errorprompt = 'Rangur innsláttur\n Sláðu inn eingöngu bókstafi.'
        subbrand=subbrand.split()
        for i in subbrand:
            if i.isalpha()==False:
                print(errorprompt)
                return False
        return True
        
        

    def is_valid_seats(self,seats):
        inputprompt = 'Fjöldi sæta: '
        errorprompt = 'Rangur innsláttur, sláðu inn heiltölu.'
        while True:
            try:
                seats = int(seats)
                if 9 < seats < 2:
                    errorprompt = 'Rangur innsláttur, of mörg sæti'
                    raise ValueError
                return seats
            except ValueError:
                pass
 #               AddCarUi.AddCarUi.get_input(errorprompt,inputprompt)

    def is_valid_transmission(self,transmission):
        inputprompt = 'Skipting b/s: '
        errorprompt = 'Rangur innsláttur.'
        while True:
            transmission = transmission.lower()
            if transmission == 'b' or 's':
                return transmission
    #        AddCarUi.AddCarUi.get_input(errorprompt,inputprompt)
            
    def get_group(self, group):
        inputprompt = 'Flokkur: '
        errorprompt = 'Rangur innsláttur, sláðu inn heiltölu'
        try:
            group = int(group)
            if 7 < group < 1:
                errorprompt = 'Rangur innsláttur.'
                raise ValueError
            return group
        except ValueError:
            pass
    #        AddCarUi.AddCarUi.get_input(errorprompt,inputprompt)

    def is_valid_cars(self):
        return self.__car_repo.get_cars()
        
        