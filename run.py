# High-level overview

# Display
## render_display: Function to show the current state of the game board.

# Game Dynamics
## start_game: Main function to initiate and control the flow of the game.
## process_turn: Manage each player's turn.
## determine_if_game_finished: Determine if the game has ended.
#### find_winner: Check if there is a winner.
##### evaluate_rows: Check rows for a win.
##### evaluate_columns: Check columns for a win.
##### evaluate_diagonals: Check diagonals for a win.
### detect_tie: Check if the game is a tie.
## switch_player: Switch the current player.



# ----- Global Variables Start -----

# Game board represented as a list of 9 elements
game_board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

# Boolean to track if the game is still in progress
game_in_progress = True

# Variable to store the winner (either 'X' or 'O') or None if no winner
game_winner = None

# Variable to keep track of the current player ('X' or 'O')
active_player = "X"

# ----- Global Variables End -----


print("""
Hey internet-traveler, it's great to have you!

Here you can experience an epic one-on-one tic-tac-toe battle with, or against, your partner or friend!
This game is designed to help you with the great decisions in life!

- You don't know where to book the next vacation?
    The winner decides!

- You don't know what to have for dinner?
    It's up to the winner to decide!

- You are not sure if you want to marry or not?
    Well, you know now how it works!

Enjoy this epic game, share it everywhere, and have fun!

In addition, feel free to visit my profile on
    [Snipverse.com](https://snipverse@fhaas.com)
and follow me on
    [LinkedIn](https://www.linkedin.com/in/-florian-haas-)!

See you at my next awesome project!
""")


# Function to display the current state of the game board
def render_display():
    for i in range(0, 9, 3):
        print(game_board[i] + '|' + game_board[i + 1] + '|' + game_board[i + 2])
    print()


# Main function to start and control the flow of the game
def start_game():
    global game_in_progress, game_winner

    # Display the initial empty board
    render_display()

    while game_in_progress:
        # Handle the turn of the current player
        process_turn(active_player)

        # Check if the game has been won or is a tie
        determine_if_game_finished()

        # The game has ended
        if game_winner:
            print(f"{game_winner} won!")
            game_in_progress = False
        elif not game_in_progress and game_winner is None:
            print("It's a tie!")

        # Switch to the other player
        switch_player()


# Handle a single turn for the given player
def process_turn(player):
    global game_board
    print(f"{player}'s turn!")

    valid_move = False
    while not valid_move:
        position = input("Choose a position from 1 to 9: ")

        # Ensure the player inputs a valid number
        if not position.isdigit():
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        position = int(position) - 1

        # Check if the chosen position is within the correct range and available
        if 0 <= position < 9:
            if game_board[position] == "-":
                valid_move = True
            else:
                print('You can\'t go there, go again!')
        else:
            print("Invalid position. Please choose a number from 1 to 9.")

    # Place the player's marker on the board
    game_board[position] = player
    # Display the updated board
    render_display()


# Check if the game is over due to a win or tie
def determine_if_game_finished():
    find_winner()
    detect_tie()


# Determine if there is a winner
def find_winner():
    global game_winner

    # Check for a win in rows, columns, and diagonals
    row_victory = evaluate_rows()
    column_victory = evaluate_columns()
    diagonal_victory = evaluate_diagonals()

    # Set the winner if there is one
    if row_victory:
        game_winner = row_victory
    elif column_victory:
        game_winner = column_victory
    elif diagonal_victory:
        game_winner = diagonal_victory


# Check if any row has all the same value and is not empty
def evaluate_rows():
    global game_in_progress

    rows = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    for row in rows:
        if game_board[row[0]] == game_board[row[1]] == game_board[row[2]] != '-':
            game_in_progress = False
            return game_board[row[0]]
    return None


# Check if any column has all the same value and is not empty
def evaluate_columns():
    global game_in_progress

    columns = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
    for col in columns:
        if game_board[col[0]] == game_board[col[1]] == game_board[col[2]] != '-':
            game_in_progress = False
            return game_board[col[0]]
    return None


# Check if any diagonal has all the same value and is not empty
def evaluate_diagonals():
    global game_in_progress

    diagonals = [(0, 4, 8), (2, 4, 6)]
    for diag in diagonals:
        if game_board[diag[0]] == game_board[diag[1]] == game_board[diag[2]] != '-':
            game_in_progress = False
            return game_board[diag[0]]
    return None


# Checks if there is a tie
def detect_tie():
    global game_in_progress
    if "-" not in game_board:
        game_in_progress = False


# Flips player, after players turn
def switch_player():
    global active_player
    active_player = 'O' if active_player == 'X' else 'X'


# Start the game
start_game()