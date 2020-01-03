"""Let's play some BlackJack"""
from People import Dealer, Player

def BlackJack():
    dealer = Dealer.EnterDealer()
    player = Player.EnterPlayer()

    for _ in range(2):
        dealer.hand.HoldCard(dealer.DealCard())
        player.hand.HoldCard(dealer.DealCard())
    dealer.PresentHand()

    player.chips.Count()
    player.ShowHand()


if __name__ == "__main__":
    BlackJack()
