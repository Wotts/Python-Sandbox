"""Let's play some BlackJack"""
import os
import time
from people import dealer, player

def BlackJack():
    """ Play a game of BlackJack """
    dlr = dealer.EnterDealer()
    plyr = player.EnterPlayer()

    while True:
        os.system("clear")
        plyr_bust = False
        dlr_bust = False
        plyr_wins = None
        bet = None

        for _ in range(2):
            # Deal two cards to both the player and dealer
            dlr.hand.hold_card(dlr.deal_card())
            plyr.hand.hold_card(dlr.deal_card())
        dlr.present_hand()

        plyr.chips.count()
        plyr.show_hand()
        plyr.hand.count_cards(verbose=True)

        # This deducts the chips from the player's credit
        bet = dlr.request_bet(plyr.chips)

        while dlr.hit_or_stand():
            os.system("clear")
            plyr.hand.hold_card(dlr.deal_card())
            dlr.present_hand(closed=True)
            plyr.show_hand()
            plyr_bust = dlr.check_bust(plyr.hand.count_cards(verbose=True))
            if plyr_bust:
                dlr.present_hand(closed=False)
                break

        if not plyr_bust:
            while dlr.hand.count_cards(0) < 17:
                #  The dealer only draws if his count is below 17
                dlr.hand.hold_card(dlr.deal_card())
                dlr_bust = dlr.check_bust(dlr.hand.count_cards())

            plyr_wins = dlr.player_wins(
                plyr.hand.count_cards(),
                dlr.hand.count_cards(),
                dlr_bust
            )

            dlr.present_hand(closed=False)
            if plyr_wins or dlr_bust:
                plyr.chips.credit += bet * 2


        # Put the cards back in the deck
        while plyr.hand:
            dlr.deck.append(plyr.hand.pop())
        while dlr.hand:
            dlr.deck.append(dlr.hand.pop())

        plyr.chips.is_broke()
        time.sleep(3)

if __name__ == "__main__":
    BlackJack()
