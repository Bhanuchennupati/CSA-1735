Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from itertools import permutations

def calculate_route_length(graph, route):
    """
    Calculate the total length of a given route.
    """
    total_length = 0
    num_cities = len(route)
    for i in range(num_cities):
        total_length += graph[route[i]][route[(i + 1) % num_cities]]
    return total_length

def travelling_salesman_problem(graph):
    """
    Solves the TSP using brute-force approach.
    """
    # Get the list of cities (nodes)
    cities = list(graph.keys())
    
    # Initialize variables to store the minimum route length and the corresponding route
    min_route_length = float('inf')
    best_route = None
    
    # Generate all possible permutations of the cities
    for perm in permutations(cities):
        # Calculate the route length for the current permutation
        current_route_length = calculate_route_length(graph, perm)
        
        # Update the minimum route length and best route if the current route is shorter
        if current_route_length < min_route_length:
            min_route_length = current_route_length
            best_route = perm
    
    return best_route, min_route_length

# Example graph represented as a distance matrix (dictionary of dictionaries)
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

# Solve the TSP for the example graph
best_route, min_route_length = travelling_salesman_problem(graph)
print("Best Route:", best_route)
print("Minimum Route Length:", min_route_length)
