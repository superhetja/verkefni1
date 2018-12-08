from services.CustomerService import CustomerService
from services.CheckInputService import CheckInput
from models.Customer import Customer
from ui.HeaderUi import Header
#from models.Clear import Clear
from models.Color import Color
from ui.InputUi import InputUi


class ShowCustomer(InputUi):
    def __init__(self):
        self.__service = CustomerService()
        self.__header = Header()
        self.__color = Color()
        self.__check_input = CheckInput()
        self.inpuut= InputUi()

    def print_menu(self):
        print(Color.BOLD+'Fletta upp viðskiptavini'+Color.END)
        print('1. Fletta viðskiptavin.')
        print('2. Birta alla viðskiptavini.')

    def show_customer_menu(self):
        '''Aðal fallið til að byrja klassan'''
        self.inpuut.clear_screen()
        self.print_menu()
        action = self.inpuut.get_number_between(1,2) #self.get_number_between(1,5)
        if action == '1':
            self.print_customer_by_search()
        else:
            self.print_all_customers()


    # def print_customer_by_name(self):
    #     name = self.inpuut.get_string(self.inpuut.NAMEPROMPT)
    #     customers = self.__service.get_matches_name(name)
    #     self.inpuut.print_list(customers)
    #     self.choice_customer(customers)
    

    def print_customer_by_search(self):
        search = input('Sláðu inn leitarstreng: ')
        customers = self.__service.get_matches(search)
        self.inpuut.print_list(customers)
        if len(customers) == 0:
            self.get_more()
        self.choice_customer(customers)

    # def print_customer_by_ssn(self):
    #     ssn = self.inpuut.get_number(self.inpuut.SSNPROMPT)
    #     customers = self.__service.get_matches_ssn(ssn)
    #     self.inpuut.print_list(customers)
    #     self.choice_customer(customers)

    # def print_customer_by_phonenr(self):
    #     phonenr = self.inpuut.get_number(self.inpuut.PHONEPROMPT)
    #     customers = self.__service.get_matches_phonenr(phonenr)
    #     self.inpuut.print_list(customers)
    #     self.choice_customer(customers)

    # def print_customer_by_email(self):
    #     email = self.inpuut.get_string(self.inpuut.EMAILPROMPT)
    #     customers = self.__service.get_matches_email(email)
    #     self.inpuut.print_list(customers)
    #     self.choice_customer(customers)

    def print_all_customers(self):
        customers = self.__service.get_customers()
        self.inpuut.print_list(customers)
        self.choice_customer(customers)

    def get_more(self):
        letter = self.inpuut.get_letter(self.inpuut.MOREPROMPT,['j','n'])
        if letter == 'j':
            self.show_customer_menu()
        else:
            pass

    def choice_customer(self, a_list):
        choice = self.inpuut.get_number_between(1,len(a_list)+1)
        chosen_customer = a_list[int(choice)-1]
        print(chosen_customer)
        print('1. Breyta viðskiptavin')
        print('2. Eyða viðskiptavin')
        print('3. Fletta upp öðrum viðskiptavin')
        print('4. Fara til baka á aðalvalmynd')
        action = self.inpuut.get_number_between(1,4)
        if action == '1':
            self.__service.remove_customer(chosen_customer)
            print('Viðskiptavini eytt')
            self.get_more()
        elif action == '2':
            self.change_customer(chosen_customer)
        elif action == '3':
            self.show_customer_menu()
        else:
            pass
    
    def change_customer(self, customer):
        print('Hverju viltu breyta?')
        print('1. Nafni')
        print('2. Kenntölu')
        print('3. Netfangi')
        print('4. Símanúmeri')
        action = self.inpuut.get_number_between(1,4)
        name = customer.get_name()
        ssn = customer.get_ssn()
        email = customer.get_email()
        phonenr = customer.get_phoneNr()
        if action == '1':
            name = self.inpuut.get_string(self.inpuut.NAMEPROMPT)
        elif action == '2':
            ssn = self.inpuut.get_number_length(self.inpuut.SSNPROMPT,10)
        elif action == '3':
            email = self.inpuut.get_email()
        else:
            phonenr = self.inpuut.get_number_length(self.inpuut.PHONEPROMPT,7)
        new_customer= Customer(name,ssn,email,phonenr)
        self.__service.change_customer(customer, new_customer)
        print('Breytingu lokið.')
        self.get_more()

         
    #choiceCostumer=input("Valinn viðskiptavinur: ")
    #þegar valið er í actions ákveðinn viðskiptavin 
    #yfirlit yfir þessum viðskiptavin

    #Varntar fjöldi leigja og hvort við viljum breyta eða eyða viðskiptavini