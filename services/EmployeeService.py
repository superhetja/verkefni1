from repositories.EmployeeRepository import EmployeeRepository

class EmployeeService:

    def __init__(self):
        pass

    def create_employee:
        fullname = input('Full nafn: ')
        while True:
            try:
            ssn = int(input(ssn)).strip()
            if len(ssn) == 10:
                break
            else:
                print('Sláðu inn gilt lykilorð!')
            except ValueError:
                print('Sláðu inn eingöngu tölur')
            
