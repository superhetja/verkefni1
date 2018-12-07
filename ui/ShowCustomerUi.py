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
        print('1. Fletta upp nafni.')
        print('2. Fletta upp kennitölu.')
        print('3. Fletta upp símanúmeri.')
        print('4. Fletta upp netfangi')
        print('5. Birta alla viðskiptavini.')

    def show_customer_menu(self):
        '''Aðal fallið til að byrja klassan'''
        self.inpuut.clear_screen()
        self.print_menu()
        action = self.inpuut.get_number_between(1,5) #self.get_number_between(1,5)
        if action == '1':
            self.print_customer_by_name()
        elif action == '2':
            self.print_customer_by_ssn()
        elif action == '3':
            self.print_customer_by_phonenr()
        elif action == '4':
            self.print_customer_by_email()
        else:
            self.print_all_customers()

    def print_customer_by_name(self):
        name = self.inpuut.get_string(self.inpuut.NAMEPROMPT)
        customers = self.__service.get_matches_name(name)
        self.inpuut.print_list(customers)
        self.get_more()
    
    def print_customer_by_ssn(self):
        ssn = self.inpuut.get_number(self.inpuut.SSNPROMPT)
        customers = self.__service.get_matches_ssn(ssn)
        self.inpuut.print_list(customers)
        self.get_more()

    def print_customer_by_phonenr(self):
        phonenr = self.inpuut.get_number(self.inpuut.PHONEPROMPT)
        customers = self.__service.get_matches_phonenr(phonenr)
        self.inpuut.print_list(customers)
        self.get_more()

    def print_customer_by_email(self):
        email = self.inpuut.get_string(self.inpuut.EMAILPROMPT)
        customers = self.__service.get_matches_email(email)
        self.inpuut.print_list(customers)
        self.get_more()

    def print_all_customers(self):
        customers = self.__service.get_customers()
        self.inpuut.print_list(customers)
        self.choice_customer(customers)
        self.get_more()

    def get_more(self):
        letter = self.inpuut.get_letter(self.inpuut.MOREPROMPT,['j','n'])
        if letter == 'j':
            self.show_customer_menu()
        else: #Skipun að fara til baka um eina valmynd
            pass


    def all_costumers(self):
        pass
    #prenta út alla viðskiptavini með þessu nafni og kt.

    def choice_customer(self, a_list):
        choice = self.inpuut.get_number_between(1,len(a_list)+1)
        index_num = int(choice)-1
        chosen_customer = a_list[index_num]
        print(chosen_customer)
        changeordel = self.inpuut.get_letter('Viltu breyta eða eyða viðskiptavini? b/e: ',['e','b'])
        if changeordel == 'e':
            self.__service.remove_customer(a_list,index_num)
         
    #choiceCostumer=input("Valinn viðskiptavinur: ")
    #þegar valið er í actions ákveðinn viðskiptavin 
    #yfirlit yfir þessum viðskiptavin

    #Varntar fjöldi leigja og hvort við viljum breyta eða eyða viðskiptavini