class CSP:
    def __init__(self, variables, domains, neighbors, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints
        self.assignment = {}
    
    def is_consistent(self, var, value):
        """
        Check if the value assignment for var is consistent with the constraints.
        """
        for neighbor in self.neighbors[var]:
            if neighbor in self.assignment and not self.constraints(var, value, neighbor, self.assignment[neighbor]):
                return False
        return True
    
    def backtrack(self):
        """
        Backtracking algorithm to solve the CSP.
        """
        if len(self.assignment) == len(self.variables):
            return self.assignment
        
        # Select an unassigned variable
        var = self.select_unassigned_variable()
        
        for value in self.domains[var]:
            if self.is_consistent(var, value):
                self.assignment[var] = value
                result = self.backtrack()
                if result:
                    return result
                del self.assignment[var]
        
        return None
    
    def select_unassigned_variable(self):
        """
        Select the next variable to assign (MRV heuristic can be implemented here).
        """
        for var in self.variables:
            if var not in self.assignment:
                return var
        return None

def map_coloring_constraints(var1, color1, var2, color2):
    """
    Constraints function to ensure no two adjacent variables have the same color.
    """
    return color1 != color2

# Define the map (graph) as regions and their neighbors
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
domains = {
    'WA': ['Red', 'Green', 'Blue'],
    'NT': ['Red', 'Green', 'Blue'],
    'SA': ['Red', 'Green', 'Blue'],
    'Q': ['Red', 'Green', 'Blue'],
    'NSW': ['Red', 'Green', 'Blue'],
    'V': ['Red', 'Green', 'Blue'],
    'T': ['Red', 'Green', 'Blue']
}
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

# Create a CSP instance
csp_instance = CSP(variables, domains, neighbors, map_coloring_constraints)

# Solve the CSP using backtracking
solution = csp_instance.backtrack()
print("Solution:", solution)
