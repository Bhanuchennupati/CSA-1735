def is_safe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col):
    # If all queens are placed, return true
    if col >= len(board):
        return True
    
    # Try placing a queen in all rows one by one
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place this queen
            board[i][col] = 1
            
            # Recur to place the rest of the queens
            if solve_nqueens_util(board, col + 1):
                return True
            
            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove the queen (backtrack)
            board[i][col] = 0
    
    # If the queen can't be placed in any row in this column col, return false
    return False

def solve_nqueens():
    n = 8
    board = [[0] * n for _ in range(n)]
    
    if not solve_nqueens_util(board, 0):
        print("Solution does not exist")
        return False
    
    print_board(board)
    return True

def print_board(board):
    for row in board:
        print(" ".join(['Q' if x == 1 else '.' for x in row]))

# Example usage:
solve_nqueens()
