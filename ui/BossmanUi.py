       
class Bossman:
    def __init__():
            pass
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