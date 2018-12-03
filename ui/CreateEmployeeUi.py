from models.Employee import Employee
class CreateEmployeeUi:

    def __init__(self):
        

    def create_empoyee():
        fullname = input('Fullt nafn: ')
        while True:
            try:
            ssn = int(input(ssn)).strip()
            if len(ssn) == 10:
                break
            else:
                print('Sláðu inn gilt lykilorð!')
            except ValueError:
                print('Sláðu inn eingöngu tölur')
        password = input('Lykilorð: ')
        email = input('Email: ')
        while True:
            admin = input('Admin y/n: ').lower()
            if admin == 'y'
                admin = True
                break
            elif admin == 'n'
                admin = False
                break
            print('Veldu rétt')
        new_employee = Employee(fullname, ssn, password, email, admin)