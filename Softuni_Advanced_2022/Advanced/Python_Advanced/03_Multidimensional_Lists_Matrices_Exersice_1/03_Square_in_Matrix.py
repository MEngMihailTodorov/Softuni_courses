n, m = map(int, input().split())
matrix = []
two_by_two_exists = 0

for _ in range(n):
    matrix.append(list(map(str, input().split())))


for i in range(n - 1):
    for j in range(m - 1):
        if matrix[i][j] == matrix[i + 1][j] == matrix[i][j + 1] == matrix[i + 1][j + 1]:
            two_by_two_exists += 1

print(two_by_two_exists)