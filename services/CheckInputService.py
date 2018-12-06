class CheckInput:

    # VAlID_BRANDS = ["Suzuki","Honda", "Hyundai","Toyota", "Volkswagen","Lexus","Renault",
    # "Mazda","Kia","Opel","Ford","Skoda","Mercedez Benz","Nissan","Jeep","Land Rover",
    # "Mitsubishi","Volvo","Citroen","VW","Audi","BMW","Chevrolet","Mini"]

    ACTION_CHOICES=[1,2,3,4,5,6,7,8]
    VALID_BRANDS = ["Suzuki","Honda", "Hyundai","Toyota", "Volkswagen","Lexus","Renault",
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
            email.index('.', atsymbol)
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

    def is_valid_between_two_letters(self, a, b, choice):
        errorprompt = 'Ekki rétt valið\nVeldu rétt'
        if choice == a or choice == b:
            return None
        else:
            return errorprompt

    #Er eh að reyna að setja þetta í fall svo að það
    #verði ekki allar þessar endurtekningar
    def eh_eh(self, sentence_input, user_errorprompt):
        while True:
            user_input = input(sentence_input)
            errorprompt = user_errorprompt(user_input)
            if not errorprompt:
                break
            else:
                print(errorprompt)