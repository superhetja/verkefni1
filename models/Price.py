class Price:
    
    price_dict = {'1': ['Standard',5000],'2': ['Luxary',8000],'3': ['Electric',7000],'4': ['Small Suv',8000],'5': ['Suv',10000],'6': ['Van',9000]}
    NAME = 0
    PRICE = 1
    TAX = 1.11
    INSURANCE = 10000
    EXTRAINSURANCE = 5000

    def get_price_one_day(self, group):
        price_wo_tax = self.price_dict[group][self.PRICE]
        return price_wo_tax * self.TAX
    
    def get_price_one_day_w_insurance(self, group):
        price_w_tax = self.get_price_one_day(group)
        return price_w_tax + self.INSURANCE