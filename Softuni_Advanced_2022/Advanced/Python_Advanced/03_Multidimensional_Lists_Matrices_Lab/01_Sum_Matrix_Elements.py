from collections import deque
n, m = map(int, (input().split(", ")))

matrix = []

for i in range(n):
    matrix.append([])
    values = deque(map(int, input().split(", ")))
    for j in range(m):
        matrix[i].append(values.popleft())

matrix_sum = 0

for j in range(n):
    matrix_sum += sum(matrix[j])

print(matrix_sum)
print(matrix)