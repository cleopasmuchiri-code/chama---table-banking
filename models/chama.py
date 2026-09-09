# chama


class Chama:
    def __init__(self, name, target_amount, deadline, frequency, members=None):
        self.name = name
        self.target_amount = target_amount
        self.deadline = deadline
        self.frequency = frequency
        self.members = members if members is not None else []

    # method to add a member to the chama
    def add_member(self, member):
        pass

    # method to calculate the expected contribution per member
    def expected_contribution_per_member(self):
        pass

    # method to calculate the total contribution made by all members
    def total_saved(self):
        pass

    # method to calculate the progress percentage towards the target amount
    def progress_percentage(self):
        pass

    # method to calculate the suggested amount per member based on the target
    def suggested_amount_per_member(self, member):
        pass
