"""Hand"""

class Hand(list):
    values = {
        '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
        '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':[1, 11]
    }

    def __init__(self):
        pass

    def HoldCard(self, card):
        self.append(card)

    def ShowCards(self, *hide):
        cards = self[0]["suit"] + self[0]["rank"] + ' '
        for card in self[1:]:
            if hide[0] == 1:
                cards += "?? "
            else:
                cards += card["suit"] + card["rank"] + ' '

        print(cards + "\n")
