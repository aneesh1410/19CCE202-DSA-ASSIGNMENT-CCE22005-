class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, source):
        # Step 1: Initialize distances and predecessors
        distances = {vertex: float('inf') for vertex in range(self.vertices)}
        predecessors = {vertex: None for vertex in range(self.vertices)}
        distances[source] = 0
        
        # Step 2: Relax edges repeatedly
        for _ in range(self.vertices - 1):
            for u, v, weight in self.edges:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u
        
        # Step 3: Check for negative cycles
        for u, v, weight in self.edges:
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative cycle")
        
        return distances, predecessors

# Example usage with a different graph:
g = Graph(6)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 1)
g.add_edge(1, 2, -2)
g.add_edge(1, 3, 3)
g.add_edge(2, 4, 4)
g.add_edge(3, 4, 2)
g.add_edge(3, 5, 1)
g.add_edge(4, 5, -1)

source_vertex = 0
distances, predecessors = g.bellman_ford(source_vertex)

print("Shortest distances from source vertex", source_vertex)
for vertex in range(g.vertices):
    print(f"Vertex {vertex}: Distance = {distances[vertex]}, Predecessor = {predecessors[vertex]}")
