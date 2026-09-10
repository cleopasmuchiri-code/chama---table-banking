# chama
import math
import datetime


class Chama:
    def __init__(self, name, target_amount, deadline, frequency, members=None):
        self.name = name
        self.target_amount = target_amount
        self.deadline = deadline
        self.frequency = frequency
        self.members = members if members is not None else []

    # method to add a member to the chama
    def add_member(self, member):
        self.members.append(member)

    # method to calculate the expected contribution per member
    def expected_contribution_per_member(self):
        return self.target_amount / len(self.members) if self.members else 0

    # method to calculate the total contribution made by all members
    def total_saved(self):
        return sum(member.savings_balance for member in self.members)

    # method to calculate the progress percentage towards the target amount
    def progress_percentage(self):
        return (self.total_saved() / self.target_amount) * 100

    # method to calculate the suggested amount per member based on the target
    def suggested_amount_per_member(self, member):
        expected = self.expected_contribution_per_member()
        remaining = expected - member.saving_balance
        days_remaining = (self.deadline - datetime.date.today()).days
        return math.ceil(remaining / days_remaining) if days_remaining > 0 else 0

    def to_dict(self):
        return {
            "name": self.name,
            "target_amount": self.target_amount,
            "deadline": self.deadline.isoformat(),
            "frequency": self.frequency,
            "members": [member.to_dict() for member in self.members],
        }

    @classmethod
    def from_dict(cls, data, member_class):
        chama = cls(
            name=data["name"],
            target_amount=data["target_amount"],
            deadline=datetime.date.fromisoformat(data["deadline"]),
            frequency=data["frequency"],
        )
        chama.members = [member_class.from_dict(m) for m in data["members"]]
        return chama
