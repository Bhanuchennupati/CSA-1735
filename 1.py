import heapq

class PuzzleState:
    def __init__(self, board, goal, moves=0, previous=None):
        self.board = board
        self.goal = goal
        self.moves = moves
        self.previous = previous
        self.cost = self.moves + self.heuristic()

    def heuristic(self):
        distance = 0
        for i in range(1, 9):
            distance += abs(self.board.index(i) % 3 - self.goal.index(i) % 3) + abs(self.board.index(i) // 3 - self.goal.index(i) // 3)
        return distance

    def get_neighbors(self):
        neighbors = []
        zero_index = self.board.index(0)
        x, y = zero_index % 3, zero_index // 3
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Left, Right, Up, Down
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_zero_index = new_y * 3 + new_x
                new_board = self.board[:]
                new_board[zero_index], new_board[new_zero_index] = new_board[new_zero_index], new_board[zero_index]
                neighbors.append(PuzzleState(new_board, self.goal, self.moves + 1, self))
        return neighbors

    def __lt__(self, other):
        return self.cost < other.cost

def solve_puzzle(start, goal):
    open_set = []
    closed_set = set()
    initial_state = PuzzleState(start, goal)
    heapq.heappush(open_set, initial_state)

    while open_set:
        current_state = heapq.heappop(open_set)
        if current_state.board == goal:
            return reconstruct_path(current_state)
        
        closed_set.add(tuple(current_state.board))

        for neighbor in current_state.get_neighbors():
            if tuple(neighbor.board) in closed_set:
                continue
            heapq.heappush(open_set, neighbor)

    return None

def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.previous
    return path[::-1]

# Example usage:
start = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

solution = solve_puzzle(start, goal)
if solution:
    print("Solution found in", len(solution) - 1, "moves:")
    for step in solution:
        print(step[:3])
        print(step[3:6])
        print(step[6:])
        print()
else:
    print("No solution found.")

