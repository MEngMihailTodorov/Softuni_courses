from collections import deque

n, m = map(int, (input().split(", ")))
matrix = []

for _ in range(n):
    row_queue = deque(map(int, input().split()))
    matrix.append(list(row_queue))

for j in range(m):
    sum = 0
    for h in range(n):
        sum += matrix[h][j]
    print(sum)