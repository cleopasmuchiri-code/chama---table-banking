# contribution
import datetime


class Contribution:
    def __init__(self, member, amount, date=None):
        self.member = member
        self.amount = amount
        self.date = date if date is not None else datetime.date.today()

    def contribute(self, amount):
        if amount <= 0:
            raise ValueError("Contribution amount must be a positive amount")
