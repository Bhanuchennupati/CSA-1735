# Define the board
board = [' ' for _ in range(9)]

# Print the board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check for a win
def check_win(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
                      (0, 4, 8), (2, 4, 6)]             # Diagonal
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Check for a draw
def check_draw():
    return ' ' not in board

# Main game loop
def play_game():
    player = 'X'
    while True:
        print_board()
        move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
        if board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[move] = player
        
        if check_win(player):
            print_board()
            print(f"Player {player} wins!")
            break
        if check_draw():
            print_board()
            print("It's a draw!")
            break
        
        player = 'O' if player == 'X' else 'X'

# Start the game
play_game()
