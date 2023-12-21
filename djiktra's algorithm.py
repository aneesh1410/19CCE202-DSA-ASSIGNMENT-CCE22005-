import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {vertex: [] for vertex in range(1, vertices + 1)}

    def add_edge(self, start, end, weight):
        self.graph[start].append((end, weight))
        self.graph[end].append((start, weight))  # Assuming an undirected graph

def dijkstra(graph, start):
    distance = {vertex: float('inf') for vertex in graph.graph}
    distance[start] = 0
    parent = {vertex: None for vertex in graph.graph}

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distance[current_vertex]:
            continue

        for neighbor, weight in graph.graph[current_vertex]:
            new_distance = distance[current_vertex] + weight

            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                parent[neighbor] = current_vertex
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distance, parent

if __name__ == "__main__":
    # Get user input for the number of vertices
    num_vertices = int(input("Enter the number of vertices: "))
    g = Graph(num_vertices)

    # Get user input for each edge
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        start, end, weight = map(int, input("Enter edge (start end weight): ").split())
        g.add_edge(start, end, weight)

    # Get user input for the start vertex
    start_vertex = int(input("Enter the start vertex: "))

    distances, parents = dijkstra(g, start_vertex)

    # Print the results
    print("\nShortest distances from vertex", start_vertex, "to all other vertices:")
    for vertex, dist in distances.items():
        print("To vertex", vertex, ":", dist)

    print("\nShortest paths:")
    for vertex, parent in parents.items():
        path = [vertex]
        while parent:
            path.insert(0, parent)
            parent = parents[parent]
        print("To vertex", vertex, ":", path)
