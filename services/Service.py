from models.Customer import Customer
from repositories.Repository import Repository
from models.Car import Car
from models.Customer import Customer
from models.Order import Order
#from repositories.CustomerRepository import CustomerRepository

class Service:
    REPO = Repository()

    def __init__(self):
        self.__repo = self.REPO
        self.__content_list = self.get_list()

    def get_list(self):
        the_list = self.__repo.read_file()
        return the_list

    def add_content(self, content):
        self.__content_list.append(content)
        self.__repo.add_content(content)

    def get_full_content(self):
        self.__content_list = self.get_list()
        return self.__content_list

    def get_matches(self, search):
        ''''Leitar instance í lista og skilar því sem það er að leita að'''
        matches = []
        full_list = self.get_full_content()
        for instance in full_list:
            if search in instance.__repr__().lower():
                matches.append(instance)
        return matches

    def remove_instance(self, instance):
        '''tekur út instance og yfirskrifar'''
        instance_id = instance.get_id()
        full_list = self.get_full_content()
        for item in full_list:
            if item.get_id() == instance_id:
                full_list.remove(item)
                self.__repo.overwrite_file(full_list)
                break
        
    
    def change_instance(self, to_remove, to_add):
        ''''Teku út instance og setur inn það sem var yfirskrifað'''
        remove_id = to_remove.get_id()
        full_list = self.get_full_content()
        for item in full_list:
            if item.get_id() == remove_id:
                full_list.remove(item)
                full_list.append(to_add)
                self.__repo.overwrite_file(full_list)
                break