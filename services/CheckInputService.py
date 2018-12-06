class CheckInput:

    VAlID_BRANDS = ["Suzuki","Honda", "Hyundai","Toyota", "Volkswagen","Lexus","Renault",
    "Mazda","Kia","Opel","Ford","Skoda","Mercedez Benz","Nissan","Jeep","Land Rover",
    "Mitsubishi","Volvo","Citroen","VW","Audi","BMW","Chevrolet","Mini"]

    
    def __init__(self):
        pass

    def is_valid_number_between(self, num, lower, higher):
        errorprompt = 'Rangur insláttur\nSláðu inn eingöngu tölustaf.'
        try:
            num = int(num)
            if num > higher or num < lower:
                errorprompt = 'Rangur innsláttur.'
                raise ValueError
            return None
        except ValueError:
            return errorprompt
            
    def is_valid_email(self, email):
        errorprompt = 'Rangt netfang\nSláðu inn gilt netfang.'
        try:
            atsymbol = email.index('@')
            dot = email.index('.', atsymbol)
            return None
        except ValueError:
            return errorprompt

    def is_valid_letter(self, letter, valid_letters):
        errorprompt = 'Rangur innsláttur'
        if letter in valid_letters:
            return None
        return errorprompt

    def is_string(self, string):
        errorprompt = 'Rangar insláttur\nSláðu inn eingöngu bókstafi.'
        string = string.split()
        for i in string:
            if i.isalpha() == False:
                return errorprompt
        return None

    def is_valid_number_length(self, num, length):
        errorprompt = 'Rangur insláttur\nSláðu inn eingöngu tölustafi.'
        try:
            num = int(num)
            if len(str(num)) != length:
                errorprompt = 'Rangur fjöldi tölustafa'
                raise ValueError
            return None
        except ValueError:
            return errorprompt
