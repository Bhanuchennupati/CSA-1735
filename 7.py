from collections import deque

def bfs(graph, start):
    # Initialize a queue with the starting node
    queue = deque([start])
    
    # Set to keep track of visited nodes to avoid processing a node more than once
    visited = set()
    
    # List to record the order in which nodes are visited
    order_of_visit = []

    # Start the BFS loop
    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.popleft()
        
        # Process the vertex if it hasn't been visited
        if vertex not in visited:
            # Mark the node as visited
            visited.add(vertex)
            
            # Append the node to the visit order list
            order_of_visit.append(vertex)
            
            # Get all adjacent nodes (neighbors) of the dequeued vertex
            # If a neighbor hasn't been visited, enqueue it
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    # Return the list of nodes in the order they were visited
    return order_of_visit

# Example graph represented as an adjacency list (dictionary)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Perform BFS starting from node 'A'
bfs_result = bfs(graph, 'A')
print("BFS Order of Visit:", bfs_result)
