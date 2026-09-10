# models

class loan:
    def __init__(self, member, amount, interest_rate):
        self.member = member
        self.amount = amount
        self.interest_rate = interest_rate
        
        self.balance = amount * (1 + interest_rate)
        self.active = True  

    # method to calculate the total amount to be repaid including interest
    def loan_balance(self):
        return self.balance

    # method to apply a repayment and reduce what's still owed
    def repay(self, amount):
        self.balance -= amount
        # once fully paid off remove the loan
        if self.balance <= 0:
            self.balance = 0
            self.active = False

    # method to check if loan is active
    def is_loan_active(self):
        return self.active