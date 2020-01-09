"""The Dealer"""
from resources import card_deck, hand

class EnterDealer():
    """ A dealer
    Has a resources.card_deck and resources.hand
    """
    deck = None
    hand = None

    def __init__(self):
        self.deck = card_deck.CardDeck()
        self.hand = hand.Hand()

    def deal_card(self):
        """ Deal a card
        Returns:
            card(dict): {"suit": "♥", "rank": "Q"}
        """
        return self.deck.take_card()

    def present_hand(self, closed=True):
        """ Present the dealer's hand
        Parameters:
            closed(bool): Hide all but the first card - default True
        """
        print("Here are the dealer's cards:")
        if closed:
            self.hand.show_cards(hide=True)
        else:
            self.hand.show_cards(hide=False)

    def request_bet(self, playerchips):
        """ Ask the player for their bet, deduct it from their credit
        Parameters:
            playerchips(object): The player's chips object

        Returns:
            bet(int): The amount of chips
        """
        while True:
            bet = input("Place your bet: ")
            try:
                int(bet)
            except ValueError:
                print("Try again...")
                continue
            if int(bet) > playerchips.credit:
                print("You don't have that much.")
                continue

            playerchips.credit -= int(bet)
            return int(bet)

    def hit_or_stand(self):
        """ Ask the player to Hit or Stand
        Returns: True when Hit, False when Stand
        """
        hit = input("Would you like to Hit(y) or Stand(n)? ")
        if hit == "y":
            return True
        return False

    def check_bust(self, count):
        """ A hand busts if over 21
        Returns: True when busts, otherwise False
        """
        if count > 21:
            print("Bust!\n")
            return True
        return False

    def player_wins(self, player, dealer, dealer_bust):
        """ Decide and show who wins
        Returns: True if the player wins, False if the dealer wins
        """
        if dealer_bust or player > dealer:
            print("You win!")
            return True
        print("Dealer wins!")
        return False
