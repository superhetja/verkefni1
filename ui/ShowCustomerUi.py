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
<<<<<<< HEAD
        print(Color.BOLD+'Look up Customer'+Color.END)
        print('1. Browse Customer.')
        print('2. Publish all Customers.')
=======
        print(Color.BOLD+'Search customer'+Color.END)
        print('1. Search customer')
        print('2. View all customers')
>>>>>>> 1efe4f279fb3caaf090afe98271d31ae6ca630da

    # def show_customer_main(self):
    #     '''Aðal fallið til að byrja klassan'''
    #     self.clear_screen()
    #     self.print_menu()
    #     action = self.get_number_between(1,2) #self.get_number_between(1,5)
    #     if action == '1':
    #         self.search_customer()
    #     else:
    #         self.print_all_customers()

    def search_customer(self):
<<<<<<< HEAD
        search = input('Enter search string: ')
=======
        search = input('Input search: ')
>>>>>>> 1efe4f279fb3caaf090afe98271d31ae6ca630da
        customers = self.__service.get_matches(search)
        self.print_list(customers)
        if len(customers) == 0:
            self.get_more()
        else:
            self.choose_customer(customers)


    def print_all_customers(self):
        customers = self.__service.get_full_content()
        self.print_list(customers)
        self.choose_customer(customers)

    # def get_more(self):
    #     letter = self.get_letter(self.MOREPROMPT,['j','n'])
    #     if letter == 'j':
    #         self.show_customer_main()
    #     else:
    #         pass
pilu
    def choose_customer(self, a_list):
        choice = self.get_number_between(1,len(a_list)+1)
        chosen_customer = a_list[int(choice)-1]
        print(chosen_customer)
<<<<<<< HEAD
        print('1. Change customer')
        print('2. Delete customer')
        print('3. Look up another customer')
        print('4. Go back to the menu')
=======
        print('1. Delete customer')
        print('2. Change customer')
        print('3. Search another customer')
        print('4. Back to main menu')
>>>>>>> 1efe4f279fb3caaf090afe98271d31ae6ca630da
        action = self.get_number_between(1,4)
        if action == '1':
            self.__service.remove_instance(chosen_customer)
            print('Customer deleted')
            self.get_more()
        elif action == '2':
            self.change_customer(chosen_customer)
        elif action == '3':
            self.search_customer()
        else:
            pass
    
    def change_customer(self, customer):
        print('What do you want to change?')
        print('1. Name')
<<<<<<< HEAD
        print('2. SSN')
        print('3. Email address')
=======
        print('2. Ssn')
        print('3. Email')
>>>>>>> 1efe4f279fb3caaf090afe98271d31ae6ca630da
        print('4. Phone number')
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
<<<<<<< HEAD
        print('Change complete.')
=======
        print('Change customer.')
>>>>>>> 1efe4f279fb3caaf090afe98271d31ae6ca630da
        self.get_more()

         
    def get_more(self):
        letter = self.get_letter(self.MOREPROMPT,['y','n'])
        if letter == 'y':
            self.search_customer()
        else:
            pass
    #choiceCostumer=input("Valinn viðskiptavinur: ")
    #þegar valið er í actions ákveðinn viðskiptavin 
    #yfirlit yfir þessum viðskiptavin

    #Varntar fjöldi leigja og hvort við viljum breyta eða eyða viðskiptavini