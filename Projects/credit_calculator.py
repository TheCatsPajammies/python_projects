import math

class CreditCalculator:
    def __init__(self):
        self.financial_data()

    def financial_data(self):
        choice = input('What do you want to calculate?\ntype "n" for number of monthly payments\ntype "a" for annuity monthly payment amount\ntype "p" for credit principal\n')
        
        if choice == "n":
            return self.number_of_payments(int(input("Enter the credit principal:\n")), 
                                            int(input("Enter the monthly payment:\n")), 
                                            float(input("Enter the credit interest:\n")))
        if choice == "a":
            return self.annuity_payment(int(input("Enter the credit principal:\n")),
                                        int(input("Enter the number of periods:\n")),
                                        float(input("Enter the credit interest:\n")))
        if choice == "p":
            return self.credit_principal(float(input("Enter the annuity payment:\n")),
                                        int(input("Enter the number of periods:\n")),
                                        float(input("Enter the credit interest:\n")))

    def number_of_payments(self, credit_principal, monthly_payment, credit_interest):
        i = credit_interest / (12 * 100)
        n = math.ceil(math.log(monthly_payment / (monthly_payment - i * credit_principal), 1 + i))
        years = n // 12
        months = n % 12
        if n == 1:
            print("It will take {} month to repay this credit!".format(months))
        elif 1 < n < 12 or n < 1:
            print("It will take {} months to repay this credit!".format(months))
        elif n % 12 > 0:
            print("It will take {} years and {} months to repay this credit!".format(years, months))
        elif n % 12 == 0 and n // 12 == 1:
            print("It will take {} year to repay this credit!".format(years))
        elif n % 12 == 0 and n // 12 > 1:
            print("It will take {} years to repay this credit!".format(years))
    
    def annuity_payment(self, credit_principal, number_of_periods, credit_interest):
        i = credit_interest / (12 * 100)
    
        monthly_payment = credit_principal * ((i * math.pow(1 + i, number_of_periods)) / (math.pow(1 + i, number_of_periods) - 1))
        print("Your monthly payment = {}!".format(math.ceil(monthly_payment)))

    def credit_principal(self, annuity_payment, number_of_periods, credit_interest):
        i = credit_interest / (12 * 100)
    
        credit_principal = annuity_payment / ((i * math.pow(1 + i, number_of_periods)) / (math.pow(1 + i, number_of_periods) - 1))
        print("Your credit principal = {}!".format(math.floor(credit_principal)))

CreditCalculator()