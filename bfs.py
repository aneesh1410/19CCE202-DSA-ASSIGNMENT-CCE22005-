import collections

# Breadth-First Search algorithm
def bfs(graph, start_node):
    visited, queue = set(), collections.deque([start_node])
    visited.add(start_node)

    while queue:
        # Dequeue a vertex from the queue
        current_node = queue.popleft()
        print(str(current_node) + " ", end="")

        # If not visited, mark it as visited, and enqueue its neighbors
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

if __name__ == '__main__':
    # Another example graph represented as an adjacency list with numbers
    numerical_graph = {
        1: [2, 3],
        2: [1, 4, 5],
        3: [1, 6, 7],
        4: [2],
        5: [2, 8],
        6: [3],
        7: [3],
        8: [5]
    }

    # Starting the BFS from node 1
    print("Breadth-First Traversal: ")
    bfs(numerical_graph, 1)


