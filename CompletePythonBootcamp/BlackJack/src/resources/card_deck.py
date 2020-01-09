"""The CardDeck"""
from random import randrange

class CardDeck(list):
    """ A deck of cards
    type: list
    """
    def __init__(self):
        self._new_shuffled_deck()

    def _new_shuffled_deck(self):
        suits = ('♥', '♦', '♠', '♣')
        ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

        for suit in suits:
            for rank in ranks:
                self.append({"suit":suit, "rank":rank})

    def take_card(self):
        """ Take a card
        Returns:
            card(dict): {"suit": "♥", "rank": "Q"}
        """
        return self.pop(randrange(len(self)))
