from models.Employee import Employee
from repositories.Repository import Repository

class EmployeeRepository(Repository):
    FILELOCATION = 'data/employees.txt'
    MODELCLASS = 'Employee'

    # def __init__(self):
    #     pass

    # def add_employee(self, employee):
    #     with open('data/employees.txt','a+' ) as aFile:
    #         aFile.write(Employee.__repr__(employee) + '\n')

    # def get_employee(self):
    #     employee = []
    #     with open("data/employees.txt") as aFile:
    #         for line in aFile.readlines():
    #             employee = eval(line.strip())
    #             employee.append(employee)
    #         return employee

