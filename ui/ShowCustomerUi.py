from services.CustomerService import CustomerService
from services.CheckInputService import CheckInput
from models.Customer import Customer
from ui.HeaderUi import Header
#from models.Clear import Clear
from models.Color import Color
from ui.Ui import Ui


class ShowCustomer(Ui):
    def __init__(self):
        Ui.__init__(self)
        self.__service = CustomerService()
        self.__header = Header()
        self.__color = Color()
        self.__check_input = CheckInput()
    #    self= InputUi()

    def print_menu(self):
        print(Color.BOLD+'Fletta upp viðskiptavini'+Color.END)
        print('1. Fletta viðskiptavin.')
        print('2. Birta alla viðskiptavini.')

    def show_customer_main(self):
        '''Aðal fallið til að byrja klassan'''
        self.clear_screen()
        self.print_menu()
        action = self.get_number_between(1,2) #self.get_number_between(1,5)
        if action == '1':
            self.search_customer()
        else:
            self.print_all_customers()

    def search_customer(self):
        search = input('Sláðu inn leitarstreng: ')
        customers = self.__service.get_matches(search)
        self.print_list(customers)
        if len(customers) == 0:
            self.get_more()
        else:
            self.choice_customer(customers)


    def print_all_customers(self):
        customers = self.__service.get_full_content()
        self.print_list(customers)
        if len(customers) == 0:
            self.get_more()
        else:
            self.choice_customer(customers)

    # def get_more(self):
    #     letter = self.get_letter(self.MOREPROMPT,['j','n'])
    #     if letter == 'j':
    #         self.show_customer_main()
    #     else:
    #         pass

    def choose_customer(self, a_list):
        choice = self.get_number_between(1,len(a_list)+1)
        chosen_customer = a_list[int(choice)-1]
        print(chosen_customer)
        print('1. Breyta viðskiptavin')
        print('2. Eyða viðskiptavin')
        print('3. Fletta upp öðrum viðskiptavin')
        print('4. Fara til baka á aðalvalmynd')
        action = self.get_number_between(1,4)
        if action == '1':
            self.__service.remove_instance(chosen_customer)
            print('Viðskiptavini eytt')
            self.get_more()
        elif action == '2':
            self.change_customer(chosen_customer)
        elif action == '3':
            self.show_customer_main()
        else:
            pass
    
    def change_customer(self, customer):
        print('Hverju viltu breyta?')
        print('1. Nafni')
        print('2. Kenntölu')
        print('3. Netfangi')
        print('4. Símanúmeri')
        action = self.get_number_between(1,4)
        name = customer.get_name()
        ssn = customer.get_ssn()
        email = customer.get_email()
        phonenr = customer.get_phoneNr()
        if action == '1':
            name = self.get_string(self.NAMEPROMPT)
        elif action == '2':
            ssn = self.get_number_length(self.SSNPROMPT,10)
        elif action == '3':
            email = self.get_email()
        else:
            phonenr = self.get_number_length(self.PHONEPROMPT,7)
        new_customer= Customer(name,ssn,email,phonenr)
        self.__service.change_instance(customer, new_customer)
        print('Breytingu lokið.')
        self.get_more()

         
    #choiceCostumer=input("Valinn viðskiptavinur: ")
    #þegar valið er í actions ákveðinn viðskiptavin 
    #yfirlit yfir þessum viðskiptavin

    #Varntar fjöldi leigja og hvort við viljum breyta eða eyða viðskiptavini