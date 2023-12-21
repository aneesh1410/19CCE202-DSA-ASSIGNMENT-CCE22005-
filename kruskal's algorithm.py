class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = [node for node in range(self.V)]
        rank = [0] * self.V

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)

        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))


# Example usage with changed inputs
g = Graph(7)
g.add_edge(0, 1, 7)
g.add_edge(0, 3, 5)
g.add_edge(1, 2, 8)
g.add_edge(1, 3, 9)
g.add_edge(1, 4, 7)
g.add_edge(2, 4, 5)
g.add_edge(3, 4, 15)
g.add_edge(3, 5, 6)
g.add_edge(4, 5, 8)
g.add_edge(4, 6, 9)
g.add_edge(5, 6, 11)

g.kruskal_algo()
