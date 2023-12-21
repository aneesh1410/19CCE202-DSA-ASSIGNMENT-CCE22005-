inf = 999999
MAX = 10
G = [
    [0, 19, 8],
    [21, 0, 13],
    [15, 18, 0]
]
S = [[0 for _ in range(MAX)] for _ in range(MAX)]
n = 3

def main():
    global n
    total_cost = prims()
    print("Spanning tree:")
    for i in range(n):
        print()
        for j in range(n):
            print(S[i][j], end=" ")
    print("\nMinimum cost =", total_cost)

def prims():
    global n
    C = [[0 for _ in range(MAX)] for _ in range(MAX)]  # Cost matrix
    u, v = 0, 0  # Variables for tracking vertices
    min_distance = 0  # Variable to store minimum distance
    dist = [0 for _ in range(MAX)]  # Distance array
    from_ = [0 for _ in range(MAX)]  # Array to store parent vertices
    visited = [0 for _ in range(MAX)]  # Array to track visited vertices
    num_edges = 0  # Counter for the number of edges
    min_cost = 0  # Total cost variable
    i = 0
    j = 0

    # Initialize the cost and spanning tree matrices
    for i in range(n):
        for j in range(n):
            if G[i][j] == 0:
                C[i][j] = inf
            else:
                C[i][j] = G[i][j]
            S[i][j] = 0

    # Initialize the distance, parent, and visited arrays
    dist[0] = 0
    visited[0] = 1
    for i in range(1, n):
        dist[i] = C[0][i]
        from_[i] = 0
        visited[i] = 0

    min_cost = 0
    num_edges = n - 1

    while num_edges > 0:
        min_distance = inf

        # Find the minimum-weight edge
        for i in range(1, n):
            if visited[i] == 0 and dist[i] < min_distance:
                v = i
                min_distance = dist[i]

        u = from_[v]
        S[u][v] = dist[v]
        S[v][u] = dist[v]
        num_edges -= 1
        visited[v] = 1

        # Update the distance and parent arrays
        for i in range(n):
            if visited[i] == 0 and C[i][v] < dist[i]:
                dist[i] = C[i][v]
                from_[i] = v

        min_cost += C[u][v]

    return min_cost

# Calling the main() method
main()
