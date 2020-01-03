"""The Dealer"""
from Resources import CardDeck, Hand

class EnterDealer():
    deck = None
    hand = None

    def __init__(self):
        self.deck = CardDeck.CardDeck()
        self.hand = Hand.Hand()

    def DealCard(self):
        return self.deck.TakeCard()

    def PresentHand(self):
        print("Here are the dealer's cards:")
        self.hand.ShowCards(1)
