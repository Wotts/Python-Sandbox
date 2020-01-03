"""Chips"""

class BuyIn():
    credit = 0
    def __init__(self):
        self.credit += 100

    def Count(self):
        print("You currently have " + str(self.credit) + " chips.")
