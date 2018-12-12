from services.CheckInputService import CheckInput
from platform import system as system_name # Returns the system/OS name
from os import system as system_call 
from models.Color import Color

class Ui:
    NAMEPROMPT = 'Name: '
    SSNPROMPT = 'Ssn: '
    PHONEPROMPT = 'Phonenumber: '
    EMAILPROMPT = 'Email: '
    MOREPROMPT = 'Do you want to continue? y/n: '
    BOOKINGDATEPROMPT = 'Booking date: '
    RETURNDATEPROMPT = "Return date: "
    CARDPROMPT = 'Card number for insurance: '
    CARNUMPROMPT = 'Car number: '
    ADMINPROMPT = 'y/n: '
   
    def __init__(self):
        self.__check_input = CheckInput()

    def get_number(self,prompt):
        '''les inn númer'''
        while True:
            num = input(prompt)
            errorprompt = self.__check_input.is_valid_number(num)
            if errorprompt == None:
                return num
            print(errorprompt)

    def get_number_between(self, lower, higher,prompt='> '):
        '''les inn lista af tolum a akvednu bili'''
        while True:
            num = input(prompt)
            errorprompt = self.__check_input.is_valid_number_between(num,lower,higher)
            if errorprompt == None:
                return num
            print(errorprompt)

    def get_email(self):
        '''les inn email'''
        while True:
            email = input(self.EMAILPROMPT)
            errorprompt = self.__check_input.is_valid_email(email)
            if errorprompt == None:
                return email
            print(errorprompt)

    def get_letter(self,prompt,valid_letters):
        '''Les inn lista af réttum stöfum'''
        while True:
            letter = input(prompt).lower()
            errorprompt = self.__check_input.is_valid_letter(letter,valid_letters)
            if errorprompt == None:
                return letter
            print(errorprompt)

    def get_string(self, prompt):
        '''les inn streng'''
        while True:
            string = input(prompt)
            errorprompt = self.__check_input.is_string(string)
            if errorprompt == None:
                return string
            print(errorprompt)

    def get_number_length(self,prompt,length):
        '''les inn lengd af numerum'''
        while True:
            num = input(prompt)
            while '-' in num:
                num = num.replace('-','')
            errorprompt = self.__check_input.is_valid_number_length(num,length)
            if errorprompt == None:
                return num
            print(errorprompt)

    def get_date(self, prompt, smaller_date=''): #Vantar að villumeðhöndla
        '''les dagsettninguna'''
        while True:
            date = input(prompt)
            errorprompt = self.__check_input.is_valid_date(date, smaller_date)
            if errorprompt == None:
                return date
            print(errorprompt)

    def clear_screen(self):
        '''
        Clears the terminal screen.
        '''
        # Clear command as function of OS
        command = "-cls" if system_name().lower()=="windows" else "clear"
        # Action
        system_call(command)

    def print_list(self,a_list):
        count = 1
        if len(a_list) == 0:
            print(Color.RED + 'No results found.' + Color.END)
        else: 
            for i in a_list:
                print(str(count)+'.',i)
                count += 1
         
    def get_carnum(self):
        '''les inn bilnumer a bil'''
        while True:
            carnum = input(self.CARNUMPROMPT).upper()
            errorprompt = self.__check_input.is_carnum(carnum)
            if errorprompt == None:
                return carnum
            print(errorprompt)

