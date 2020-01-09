"""The Player"""
from resources import chips, hand

class EnterPlayer():
    """ A player
    Has a resources.chips and resources.hand
    """
    chips = None
    hand = None

    def __init__(self):
        self.chips = chips.BuyIn()
        self.hand = hand.Hand()

    def show_hand(self):
        """ Show the player's cards """
        print("Here are your cards:")
        self.hand.show_cards(hide=False)
