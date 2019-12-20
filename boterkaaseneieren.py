from random import randrange
import os

def play():
    def printboard():
        os.system('clear')
        print("Here's the board:\n")
        for e in (2, 1, 0):
            print(f"{b[e*3+1]}|{b[e*3+2]}|{b[e*3+3]}")
            print("-+-+-") if e else print("")

    def choose_beginner():
        x_or_o = randrange(2)
        return "X" if x_or_o == 1 else "O"

    def player_input(turn):
        def choice():
            while True:
                c = input(f'Player {turn}, place your {turn}: ')
                try:
                    int(c); return int(c)
                except ValueError:
                    wrong_input(); continue

        s = choice()
        while not 1 <= s <= 9:
            wrong_input()
            s = choice()
        else:
            return s

    def wrong_input():
        printboard()
        print("Between 1 and 9...")

    def check_for_winner():
        winning = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
            [2, 5, 8], [3, 6, 9], [1, 5, 9], [7, 5, 3]
        ]
        for i in winning:
            if b[i[0]] == b[i[1]] == b[i[2]]:
                return True

    b = {}
    for i in (range(9)):
        b[i+1] = i+1

    winner = False
    turn   = choose_beginner()

    while not winner:
        printboard()
        location = player_input(turn)
        if (b[location] not in {"X", "O"}):
            b[location] = turn
            if check_for_winner():
                winner = turn
                break
            turn = "X" if turn == "O" else "O"

    printboard(); print(f"{winner} wins this game!")

play()

