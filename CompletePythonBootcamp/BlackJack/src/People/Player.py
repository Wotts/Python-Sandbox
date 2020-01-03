"""The Player"""
from Resources import Chips, Hand

class EnterPlayer():
    chips = None
    hand = None

    def __init__(self):
        self.chips = Chips.BuyIn()
        self.hand = Hand.Hand()

    def ShowHand(self):
        print("Here are your cards:")
        self.hand.ShowCards(0)

