from services.CheckInputService import CheckInput
from platform import system as system_name # Returns the system/OS name
from os import system as system_call 

class Ui:
    NAMEPROMPT = 'Nafn: '
    SSNPROMPT = 'Kennitala: '
    PHONEPROMPT = 'Símanúmer: '
    EMAILPROMPT = 'Netfang: '
    MOREPROMPT = 'Viltu halda áfram j/n: '
    BOOKINGDATEPROMPT = 'Sláðu inn úttektardag: '
    RETURNDATEPROMPT = "Sláðu inn skiladag: "
    CARDPROMPT = 'Kortanúmer: '
    CARNUMPROMPT = 'Bílnúmer: '
    ADMINPROMPT = 'j/n: '
   

    def __init__(self):
        self.__check_input = CheckInput()

    def get_number(self,prompt):
        while True:
            num = input(prompt)
            errorprompt = self.__check_input.is_valid_number(num)
            if errorprompt == None:
                return num
            print(errorprompt)

    def get_number_between(self, lower, higher,prompt='> '):
        while True:
            num = input(prompt)
            errorprompt = self.__check_input.is_valid_number_between(num,lower,higher)
            if errorprompt == None:
                return num
            print(errorprompt)

    def get_email(self):
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
        while True:
            string = input(prompt)
            errorprompt = self.__check_input.is_string(string)
            if errorprompt == None:
                return string
            print(errorprompt)

    def get_number_length(self,prompt,length):
        while True:
            num = input(prompt)
            errorprompt = self.__check_input.is_valid_number_length(num,length)
            if errorprompt == None:
                return num
            print(errorprompt)

    def get_date(self, prompt): #Vantar að villumeðhöndla
        while True:
            date =input(prompt)
            errorprompt = self.__check_input.is_valid_date(date)
            if errorprompt == None:
                return date
            print(errorprompt)

    def get_admin(self, prompt):
        while True:
            admin = input(prompt).capitalize()
            errorprompt = self.__check_input.is_valid_between_two_letters('j', 'n', admin)
            if errorprompt == None:
                return admin
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
            print('Engar niðurstöður fundust.')
        else: 
            for i in a_list:
                print(str(count)+'.',i)
                count += 1
         
    def get_carnum(self):
        while True:
            carnum = input(self.CARNUMPROMPT)
            errorprompt = self.__check_input.is_carnum(carnum)
            if errorprompt == None:
                return carnum
            print(errorprompt)

    def get_more(self):
        letter = self.get_letter(self.MOREPROMPT,['j','n'])
        if letter == 'j':
            self.show_customer_main()
        else:
            pass