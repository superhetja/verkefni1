import datetime

class CheckInput:

    #ACTION_CHOICES=[1,2,3,4,5,6,7,8]
    VALID_BRANDS = ["Suzuki","Honda", "Hyundai","Toyota", "Volkswagen","Lexus","Renault",
    "Mazda","Kia","Opel","Ford","Skoda","Mercedez Benz","Nissan","Jeep","Land Rover",
    "Mitsubishi","Volvo","Citroen","VW","Audi","BMW","Chevrolet","Mini"]
    
    def __init__(self):
        pass

    def is_valid_number_between(self, num, lower, higher):
        '''Tekur inn breytu og bil og segir til um hvort breytan se heiltala og se a bilinu'''
        errorprompt = 'Incorrect input\nEnter numbers only.'
        try:
            num = int(num)
            if num > higher or num < lower:
                errorprompt = 'Input out of range.'
                raise ValueError
            return None
        except ValueError:
            return errorprompt
            
    def is_valid_email(self, email):
        '''Tekur inn netfang og athugar hvort thad se gilt'''
        errorprompt = 'Incorrect email\nEnter a valid email address.'
        try:
            atsymbol = email.index('@')
            email.index('.', atsymbol)
            return None
        except ValueError:
            return errorprompt

    def is_valid_number(self,num):
        '''Tekur inn breytu og athugar hvort ad hun se heiltala'''
        errorprompt = 'Incorrect input\nEnter numbers only.'
        try:
            int(num)
            return None
        except ValueError:
            return errorprompt

    def is_valid_letter(self, letter, valid_letters):
        '''Tekur inn staf og lista af gildum stofum og athugar hvort stafurinn se gildur stafur'''
        errorprompt = 'Incorrect input'
        if letter in valid_letters:
            return None
        return errorprompt

    def is_string(self, string):
        '''Tekur inn streng og athugar hvort ad allt i strengnum se stafur'''
        errorprompt = 'Incorrect input\nEnter letters only.'
        string = string.split()
        for i in string:
            if i.isalpha() == False:
                return errorprompt
        return None

    def is_valid_number_length(self, num, length):
        '''Tekur inn breytu og lengd a streng og athugar hvort að breytan se heiltala og se rett legnd'''
        errorprompt = 'Incorrect input\nEnter numbers only.'
        try:
            num = int(num)
            if len(str(num)) != length:
                errorprompt = 'Incorrect number of digits'
                raise ValueError
            return None
        except ValueError:
            return errorprompt

    def is_valid_date(self, date):
        '''Tekur inn dagsetningu og athugar hvort ad hun se gild'''
        errorprompt = 'Invalid date'
        try:
            if '.' in date:
                seperator = '.'
            elif '/' in date:
                seperator = '/' 
            elif '-' in date:
                seperator = '-'
            day,month,year = date.split(seperator)
            datetime.datetime(int(year),int(month),int(day))
            return None
        except ValueError:
            return(errorprompt)

    def is_carnum(self, carnum):
        errorprompt = 'Incorrect input'
        if len(carnum) == 5 and carnum.isalnum():
            return None
        return errorprompt
