from models.Customer import Customer
from repositories.Repository import Repository
#from repositories.CustomerRepository import CustomerRepository

class Service:
    REPO = Repository()

    def __init__(self):
        self.__repo = self.REPO

    def add_content(self, content):
        self.__repo.add_content(content)

    def get_full_content(self):
        return self.__repo.get_content()

    def get_matches(self, search):
        matches = []
        full_list = self.get_full_content()
        for instance in full_list:
            if search in instance.__repr__():
                matches.append(instance)
        return matches

    def remove_instance(self, instance):
        full_list = self.get_full_content()
        full_list.remove(instance)
        self.__repo.overwrite_file(full_list)
    
    def change_instance(self, to_remove, to_add):
        full_list = self.get_full_content()
        full_list.remove(to_remove)
        full_list.append(to_add)
        self.__repo.overwrite_file(full_list)