n = int(input())
matrix = []
primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for i in range(n):
    matrix.append(list(map(int, input().split())))

for h in range(n):
    primary_diagonal_sum += matrix[h][h]

for k in range(n):
    for l in range(n):
        if (k + l) == n - 1:
            secondary_diagonal_sum += matrix[k][l]

print(abs(secondary_diagonal_sum - primary_diagonal_sum))