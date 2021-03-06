"""TicTacToe"""
from os import system
from random import randrange
from collections import defaultdict
from colorama import Style, Fore

class Board():
    """Keep track of the Board's current state"""
    board = {}
    winner = False

    def __init__(self):
        """Create and show the playingboard"""
        for i in range(9):
            self.board[i+1] = i+1
        self.show()

    def show(self):
        """Show the playingboard in it's current state"""
        system('clear')
        print("\n"*3)
        for i in (2, 1, 0):
            print(f"\t{self.board[i*3+1]}|{self.board[i*3+2]}|{self.board[i*3+3]}")
            print("\t-+-+-") if i else print("")

    def check_for_winner(self):
        """See if we have a winner yet"""
        winning = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
            [2, 5, 8], [3, 6, 9], [1, 5, 9], [7, 5, 3]
        ]
        for i in winning:
            if self.board[i[0]] == self.board[i[1]] == self.board[i[2]]:
                self.winner = True

    def place_marker(self, turn, location):
        """Place an 'X' or 'O' on the board"""
        if (self.board[location] not in {"X", "O"}):
            self.board[location] = turn
            return True

        return False

class PlayerTurn():
    """Keep track of turns"""
    turn = None

    def __init__(self):
        """Randomly choose who starts"""
        self.turn = "X" if randrange(2) == 1 else "O"

    def next_turn(self):
        """Swap turns"""
        self.turn = "X" if self.turn == "O" else "O"
        return self.turn


class PlayerInput():
    """Handle the player's input"""
    def request_input(self, turn):
        """Validate the player's pick"""
        while True:
            move = self.choice(turn)
            if not 1 <= move <= 9:
                self.wrong_input(move)
            else:
                break

        return move

    def choice(self, turn):
        """Ask the player to take their pick"""
        while True:
            pick = input(f'Player {turn}, place your {turn}: ')
            try:
                int(pick)
                return int(pick)
            except ValueError:
                self.wrong_input(pick)
                continue

    def wrong_input(self, wrong):
        """Notify about wrong input"""
        print(Fore.RED + f"{wrong} is not between 1 and 9..." + Style.RESET_ALL)


def play():
    """Play a game of TicTacToe"""
    score_count = defaultdict(int)

    while True:
        board = Board()
        p_turn = PlayerTurn()
        p_input = PlayerInput()

        for _ in range(9):
            while True:
                mark_placed = board.place_marker(
                    p_turn.turn,
                    p_input.request_input(p_turn.turn)
                )
                if mark_placed is True:
                    break
                print(Fore.YELLOW + "You can't do that." + Style.RESET_ALL)

            board.check_for_winner()
            board.show()
            if not board.winner:
                p_turn.next_turn()
            else:
                print(
                    Style.BRIGHT + Fore.GREEN + f"{p_turn.turn} wins this game!" + Style.RESET_ALL
                )
                score_count[p_turn.turn] += 1
                break

        if not board.winner:
            print("Nobody wins.")

        again = input("Play again? (y/n) ")
        if again.lower() in "yes":
            pass
        else:
            break

    print(dict(score_count))
    exit("Thanks for playing!")

if __name__ == "__main__":
    # Let's play!
    play()
