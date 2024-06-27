import math

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

# Get available moves
def get_available_moves():
    return [i for i in range(9) if board[i] == ' ']

# Minimax algorithm
def minimax(is_maximizing):
    if check_win('X'):
        return -1
    elif check_win('O'):
        return 1
    elif check_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves():
            board[move] = 'O'
            score = minimax(False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves():
            board[move] = 'X'
            score = minimax(True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

# Get the best move for the computer
def get_best_move():
    best_score = -math.inf
    best_move = None
    for move in get_available_moves():
        board[move] = 'O'
        score = minimax(False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# Main game loop
def play_game():
    player = 'X'
    while True:
        print_board()
        if player == 'X':
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] != ' ':
                print("Invalid move. Try again.")
                continue
        else:
            move = get_best_move()
            print(f"Computer chooses position {move + 1}")

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
