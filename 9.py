import heapq

def a_star(graph, start, goal):
    # Priority queue to store nodes to explore
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    # Dictionary to store the cost from the start node to the current node
    g_costs = {start: 0}
    
    # Dictionary to store the estimated cost from the start node to the goal (f = g + h)
    f_costs = {start: heuristic(start, goal)}
    
    # Dictionary to store the path
    came_from = {}
    
    while open_list:
        # Get the node with the lowest f_cost
        current_f, current_node = heapq.heappop(open_list)
        
        # If the goal is reached, reconstruct and return the path
        if current_node == goal:
            return reconstruct_path(came_from, current_node)
        
        # Explore neighbors
        for neighbor, cost in graph[current_node].items():
            tentative_g_cost = g_costs[current_node] + cost
            
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                # Update the path and costs
                came_from[neighbor] = current_node
                g_costs[neighbor] = tentative_g_cost
                f_costs[neighbor] = tentative_g_cost + heuristic(neighbor, goal)
                
                # Add the neighbor to the open list
                heapq.heappush(open_list, (f_costs[neighbor], neighbor))
    
    return None  # Return None if no path is found

def heuristic(node, goal):
    """
    Heuristic function: estimate the cost from the current node to the goal.
    Example: using Manhattan distance for grid-based maps.
    """
    (x1, y1) = node
    (x2, y2) = goal
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current_node):
    """
    Reconstruct the path from the start node to the goal node.
    """
    path = [current_node]
    while current_node in came_from:
        current_node = came_from[current_node]
        path.append(current_node)
    path.reverse()
    return path

# Example graph represented as an adjacency list (dictionary of dictionaries)
graph = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (1, 1): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1},
    (1, 1): {(1, 0): 1, (0, 1): 1, (2, 1): 1},
    (2, 1): {(1, 1): 1, (2, 2): 1},
    (2, 2): {(2, 1): 1}
}

# Define the start and goal nodes
start = (0, 0)
goal = (2, 2)

# Perform A* search
path = a_star(graph, start, goal)
print("Path from start to goal:", path)
