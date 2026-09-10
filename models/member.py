# models/member.py

from models.loan import loan


class Member:
    LOAN_LIMIT = 50000  
    INTEREST_RATE = 0.05 

    def __init__(self, name, role, password):
        self.name = name
        self.role = role
        self.password = password
        self.savings_balance = 0 
        self.loan_balance = 0
        self.loan = None  

    # contribution method
    def contribute(self, amount):
        self.savings_balance += amount

    # request loan method
    def request_loan(self, amount):
        if amount > self.LOAN_LIMIT:
            raise ValueError(
                f"Requested amount {amount} exceeds loan limit of {self.LOAN_LIMIT}"
            )
        self.loan = loan(self, amount, self.INTEREST_RATE)
        self.loan_balance = self.loan.loan_balance()

    # repay loan method
    def repay_loan(self, amount):
        if self.loan is not None:
            self.loan.repay(amount)
            self.loan_balance = self.loan.loan_balance()

    # check if the member currently has an active loan
    def is_loan_active(self):
        if self.loan is None:
            return False
        return self.loan.is_loan_active()