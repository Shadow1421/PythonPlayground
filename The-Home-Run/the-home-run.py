import random

# Function to display the game board
def display_board(player_a, player_b):
    board = []
    for i in range(1, 31):
        if i == player_a:
            board.append(' A ')
        elif i == player_b:
            board.append(' B ')
        else:
            board.append('{:02d}'.format(i))
    print('--------------------------')
    print(' '.join(board[:5]))
    print('--------------------------')
    print(' '.join(board[5:10][::-1]))
    print('--------------------------')
    print(' '.join(board[10:15]))
    print('--------------------------')
    print(' '.join(board[15:20][::-1]))
    print('--------------------------')
    print(' '.join(board[20:25]))
    print('--------------------------')
    print(' '.join(board[25:][::-1]))
    print('--------------------------')

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Function to start and play the game
def play_game():
    player_a = 0
    player_b = 0
    current_player = 'A'

    while True:
        print("\nPress 'Y' to roll the dice:")
        choice = input()

        if choice.upper() == 'Y':
            dice_roll = roll_dice()
            print("Dice rolled:", dice_roll)

            if current_player == 'A':
                player_a += dice_roll
                if player_a > 30:
                    player_a = 30
                if player_a == player_b:
                    player_b = 0
                    print("Player B moved back to start!")
            else:
                player_b += dice_roll
                if player_b > 30:
                    player_b = 30
                if player_b == player_a:
                    player_a = 0
                    print("Player A moved back to start!")

            if dice_roll == 6:
                print("Extra move for Player", current_player)

            display_board(player_a, player_b)

            if player_a == 30:
                print("Player A wins!")
                break
            elif player_b == 30:
                print("Player B wins!")
                break

            current_player = 'B' if current_player == 'A' else 'A'

# Start the game
play_game()
