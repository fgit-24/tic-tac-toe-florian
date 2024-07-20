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




# Game board represented as a list of 9 elements
game_board = ['-', '-', '-',
              '-', '-', '-',
              '-', '-', '-']

      
# Function to display the current state of the game board

def current_state():
    for i in range(0, 9, 3):
        print(game_board[i] + '|' + game_board[i + 1] + '|' + game_board[i + 2])
    print()

current_state()


valid_move = False
while not valid_move:
    # Get user input for position
    postition = input("Enter a number between 1 and 9: ")

    # Ensure the player inputs a valid number
    if position not in [str(i) for i in range(1, 10)]:
        print("Invalid input. Please choose a valid position from 1 to 9.")
        continue

    # -1 Because our list starts with the index of 0
    position = int(position) - 1

    # Check if the chosen position is available
    if game_board[position] == "-":
        valid_move = True
    else:
        print('You can\'t go there, go again!')

    # Place the player's marker on the board
    game_board[position] = player
    # Display the updated board