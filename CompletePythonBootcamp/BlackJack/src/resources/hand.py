"""Hand"""

class Hand(list):
    """ An empty hand
    type: list
    """
    values = {
        '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
        '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':[1, 11]
    }

    def __init__(self):
        pass

    def hold_card(self, card):
        """ Hold a card
        Parameters:
            card(dict): {"suit": "♥", "rank": "Q"}
        """
        self.append(card)

    def show_cards(self, hide=False):
        """ Show the player's cards
        Parameters:
            hide(bool): Hide all but the first card - default False
        """
        cards = self[0]["suit"] + self[0]["rank"] + ' '
        for card in self[1:]:
            if hide == True:
                cards += "?? "
            else:
                cards += card["suit"] + card["rank"] + ' '

        print(cards + "\n")

    def count_cards(self, verbose=False):
        """ Count the value of the player's cards
        Parameters:
            verbose(bool): Show the count

        Returns
            count(int): The total value
        """
        count = 0
        ace_present = False
        for card in self:
            if card["rank"] == "A":
                count += self.values["A"][0] if count > 21 or ace_present else self.values["A"][1]
            else:
                count += self.values[card["rank"]]
        if verbose:
            print(f"Your cards are worth: {count}\n")
        return count
