from repositories.CustomerRepository import CustomerRepository
from models.Customer import Customer
from services.Service import Service



class CustomerService(Service):
    REPO = CustomerRepository()

    def __init__(self):
        Service.__init__(self)