import numpy as np

INF = float('inf')

n = int(input("Enter the number of vertices: "))
a = np.ndarray((n, n), dtype=float)
c = np.ndarray((n, n), dtype=float)

for i in range(n):
    for j in range(n):
        value = input(f"Enter the number for row {i+1} and column {j+1} (enter 'INF' for infinity): ")
        if value.upper() == 'INF':
            a[i][j] = INF
        else:
            a[i][j] = float(value)

for i in range(n):
    for j in range(n):
        if i == j:
            c[i][j] = 0
        else:
            c[i][j] = a[i][j]
for k in range(n):
    for i in range(n):
        for j in range(n):
            c[i][j] = min(c[i][j], c[i][k] + c[k][j])

result=c
print("Shortest paths matrix:")
print(result)
