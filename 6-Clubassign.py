import math
from queue import PriorityQueue

class Node:
    def __init__(self, cost, level, assigned):
        self.cost = cost
        self.level = level
        self.assigned = assigned
    
    def __lt__(self, other):
        return self.cost < other.cost  # Define comparison for priority queue

def calculate_cost_matrix(cost_matrix):
    """Calculate the minimum cost to assign clubs."""
    n = len(cost_matrix)
    
    # Create a priority queue to store the nodes of the search tree
    pq = PriorityQueue()
    
    # Create the root node
    root = Node(cost=0, level=0, assigned=[-1] * n)
    pq.put(root)
    
    # Initialize the minimum cost to a large number
    min_cost = math.inf
    min_assignment = []
    
    while not pq.empty():
        # Get the node with the minimum cost
        node = pq.get()
        
        if node.level == n:
            # If we've assigned all clubs, check if we found a new minimum
            if node.cost < min_cost:
                min_cost = node.cost
                min_assignment = node.assigned.copy()
            continue
        
        # Explore possible assignments for the current student
        for j in range(n):
            if j not in node.assigned:
                # Calculate the cost of assigning student at 'node.level' to club 'j'
                new_cost = node.cost + cost_matrix[node.level][j]
                new_assigned = node.assigned.copy()
                new_assigned[node.level] = j
                
                # Create the new node
                new_node = Node(cost=new_cost, level=node.level + 1, assigned=new_assigned)
                
                # Only add the node if it has the potential to be a minimum
                if new_cost < min_cost:
                    pq.put(new_node)
    
    return min_cost, min_assignment

def main():
    # Input number of students (and clubs)
    n = int(input("Enter the number of students (and clubs): "))
    
    # Input cost matrix
    cost_matrix = []
    print("Enter the cost matrix (row-wise):")
    for i in range(n):
        row = list(map(int, input("Row",i + 1)))
        cost_matrix.append(row)
    
    # Calculate the minimum cost and assignment
    min_cost, assignment = calculate_cost_matrix(cost_matrix)
    
    print("\nMinimum cost of assignment: ",min_cost)
    print("Optimal assignment of students to clubs:")
    for i in range(len(assignment)):
        print("  Student ", {i + 1} ,"-> Club " ,assignment[i] + 1)

if __name__ == "__main__":
    main()

