# Import
import os
import time

# Define the board
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Define players
human = "X"
computer = "O"

# Other Global Variables
best_move = 0


# Print the header
def print_header():
    print("Welcome to tic-tac-toe! To win, you must get three of your symbols in a row, whether it be diagonally,")
    print("horizontally, or vertically.")


# Printing the board
def print_board():
    print("   |   |   ")
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + "  ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + "  ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + "  ")
    print("   |   |   ")


def check_for_tie(game):
    filled = True
    for i in range(len(game)):
        if game[i] == " ":
            filled = False

    if filled:
        if not check_for_win(game, "X") and not check_for_win(game, "O"):
            return True
        else:
            return False


def check_for_win(game, player):
    if ((game[0] == player and game[1] == player and game[2] == player) or
            (game[3] == player and game[4] == player and game[5] == player) or
            (game[6] == player and game[7] == player and game[8] == player) or
            (game[0] == player and game[3] == player and game[6] == player) or
            (game[1] == player and game[4] == player and game[7] == player) or
            (game[2] == player and game[5] == player and game[8] == player) or
            (game[0] == player and game[4] == player and game[8] == player) or
            (game[2] == player and game[4] == player and game[6] == player)):
        return True
    else:
        return False


def minimax(game, player):
    game_copy = game
    game_score = score(game_copy)
    if game_score != -100:
        return game_score

    scores = []
    moves = []
    global best_move

    available_moves = []
    for i in range(len(game_copy)):
        if game_copy[i] == " ":
            available_moves.append(i)

    if player == "X":
        opponent = "O"
    else:
        opponent = "X"

    for i in available_moves:
        game_copy[i] = player
        scores.append(minimax(game_copy, opponent))
        moves.append(i)
        game_copy[i] = " "

    if player == computer:
        max_score_i = 0
        for i in range(len(scores)):
            if scores[i] > scores[max_score_i]:
                max_score_i = i
        best_move = moves[max_score_i]
        return scores[max_score_i]
    else:
        min_score_i = 0
        for i in range(len(scores)):
            if scores[i] < scores[min_score_i]:
                min_score_i = i
        return scores[min_score_i]


def score(game):
    computer_won = check_for_win(game, computer)
    human_won = check_for_win(game, human)
    if computer_won:
        return 10
    elif human_won:
        return -10
    elif check_for_tie(game):
        return 0
    # Game hasn't ended yet
    else:
        return -100


def human_vs_human():
    game_ended = False
    while not game_ended:
        os.system("cls")
        print_board()

        # Player 1's move
        valid = False
        while not valid:
            choice = input("Player 1: please choose which square you would like to put an X: ")
            is_int = False
            while not is_int:
                try:
                    choice = int(choice)
                    is_int = True
                except ValueError:
                    choice = input("Please enter a valid number (from 1 and 9): ")
                    is_int = False
            if choice < 1 or choice > 9:
                print("This value is not valid.")
                continue

            if board[choice - 1] == " ":
                board[choice - 1] = "X"
                valid = True
            else:
                print("Sorry, that square is not empty.")
                time.sleep(1)

        print_board()
        
        win = check_for_win(board, "X")
        if win:
            print("X has won the game.")
            game_ended = True
            continue
        else:
            tie = check_for_tie(board)
            if tie:
                game_ended = True
                print("The game was a tie.")

        # Player 2's move
        valid = False
        while not valid:
            choice = input("Player 2: please choose which square you would like to put an O: ")
            is_int = False
            while not is_int:
                try:
                    choice = int(choice)
                    is_int = True
                except ValueError:
                    choice = input("Please enter a valid number (from 1 and 9): ")
                    is_int = False
            if choice < 1 or choice > 9:
                print("This value is not valid.")
                continue

            if board[choice - 1] == " ":
                board[choice - 1] = "O"
                valid = True
            else:
                print("Sorry, that square is not empty.")
                time.sleep(1)

        win = check_for_win(board, "O")
        if win:
            print("O has won the game.")
            game_ended = True
        else:
            tie = check_for_tie(board)
            if tie:
                game_ended = True
                print("The game was a tie.")


def human_vs_computer():
    game_ended = False

    while not game_ended:
        os.system("cls")
        print_board()

        # Human's move
        valid = False
        while not valid:
            choice = input("Player 1: please choose which square you would like to put an X: ")
            is_int = False
            while not is_int:
                try:
                    choice = int(choice)
                    is_int = True
                except ValueError:
                    choice = input("Please enter a valid number (from 1 and 9): ")
                    is_int = False
            if choice < 1 or choice > 9:
                print("This value is not valid.")
                continue

            if board[choice - 1] == " ":
                board[choice - 1] = "X"
                valid = True
            else:
                print("Sorry, that square is not empty.")
                time.sleep(1)

        win = check_for_win(board, "X")
        if win:
            print("X has won the game.")
            game_ended = True
        else:
            tie = check_for_tie(board)
            if tie:
                game_ended = True
                print("The game was a tie.")

        # Computer's move
        minimax(board, "O")
        board[best_move] = "O"

        print_board()

        win = check_for_win(board, "O")
        if win:
            print("O has won the game.")
            game_ended = True
            continue
        else:
            tie = check_for_tie(board)
            if tie:
                game_ended = True
                print("The game was a tie.")


os.system("cls")
print_header()
opponent_choice = str(input("Who would you like to play with (type \"computer\" or \"player\")? "))
opponent_choice = opponent_choice.lower()

if opponent_choice == "computer":
    human_vs_computer()
else:
    human_vs_human()
