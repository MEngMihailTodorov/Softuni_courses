from collections import deque

n, m = map(int, (input().split(", ")))
matrix = []

for _ in range(n):
    row_queue = deque(map(int, input().split(", ")))
    matrix.append(list(row_queue))

max_sum = 0

for i in range(n-1):
    sum = 0
    for j in range(m-1):
        sum = matrix[i][j + 1] + matrix[i + 1][j] + matrix[i][j] + matrix[i + 1][j + 1]
        if sum > max_sum:
            max_sum = sum
            saved_i = i
            saved_j = j


print(f"{matrix[saved_i][saved_j]} {matrix[saved_i][saved_j + 1]}")
print(f"{matrix[saved_i + 1][saved_j]} {matrix[saved_i + 1][saved_j + 1]}")
print(max_sum)