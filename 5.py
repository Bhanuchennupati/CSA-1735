from collections import deque

# State class to represent the state of the problem
class State:
    def __init__(self, missionaries, cannibals, boat_left):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat_left = boat_left
    
    def is_valid(self):
        if self.missionaries < 0 or self.missionaries > 3:
            return False
        if self.cannibals < 0 or self.cannibals > 3:
            return False
        if self.missionaries > 0 and self.missionaries < self.cannibals:
            return False
        if 3 - self.missionaries > 0 and 3 - self.missionaries < 3 - self.cannibals:
            return False
        return True
    
    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and not self.boat_left
    
    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat_left == other.boat_left
    
    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat_left))
    
    def __str__(self):
        return f"({self.missionaries}, {self.cannibals}, {'Left' if self.boat_left else 'Right'})"

# Function to get possible moves from a state
def get_moves(state):
    moves = []
    if state.boat_left:
        for m in range(1, 3 + 1):
            for c in range(0, m + 1):
                new_state = State(state.missionaries - m, state.cannibals - c, not state.boat_left)
                if new_state.is_valid():
                    moves.append(new_state)
    else:
        for m in range(1, 3 + 1):
            for c in range(0, m + 1):
                new_state = State(state.missionaries + m, state.cannibals + c, not state.boat_left)
                if new_state.is_valid():
                    moves.append(new_state)
    return moves

# Function to perform BFS to find the solution
def bfs_search(initial_state):
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(initial_state)
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state.is_goal():
            return path + [current_state]
        
        for move in get_moves(current_state):
            if move not in visited:
                visited.add(move)
                queue.append((move, path + [current_state]))
    
    return None

# Main function to solve the problem
def solve_missionaries_cannibals():
    initial_state = State(3, 3, True)
    solution_path = bfs_search(initial_state)
    
    if solution_path:
        print("Solution Found:")
        for i, state in enumerate(solution_path):
            print(f"Step {i + 1}: {state}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    solve_missionaries_cannibals()
