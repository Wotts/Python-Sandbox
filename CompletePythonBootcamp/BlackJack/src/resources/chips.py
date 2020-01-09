"""Chips"""

class BuyIn():
    credit = 0
    def __init__(self):
        self.credit += 100

    def count(self):
        """ Show the player's credit """
        print("You currently have " + str(self.credit) + " chips.")

    def is_broke(self):
        """ See if the player ran out of chips """
        if self.credit == 0:
            exit("You're broke, go home!")
