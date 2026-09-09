# loans


class Loan:
    def __init__(self, member, amount, interest_rate):
        self.member = member
        self.amount = amount
        self.interest_rate = interest_rate

    # method to calculate the total amount to be repaid including interest
    def loan_balance(self):
        pass

    # method to calculate the monthly repayment amount based on loan amount and interest rate
    def repay(self, amount):
        pass

    # method to check if loan is active
    def is_loan_active(self):
        pass
