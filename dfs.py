from collections import defaultdict

class Graph:
    def __init__(self):
        # Default dictionary to store the graph
        self.graph = defaultdict(list)

    # Function to add an edge to the graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive utility function for DFS
    def DFSUtil(self, v, visited):
        # Mark the current node as visited and print it
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)

    # The main DFS traversal function
    def DFS(self, v):
        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function to print DFS traversal
        self.DFSUtil(v, visited)

# Driver's code
if __name__ == "__main__":
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 6)
    g.addEdge(3, 7)
    g.addEdge(4, 8)
    g.addEdge(5, 9)

    print("Depth-First Traversal (starting from vertex 1):")
    
    # Function call
    g.DFS(1)

