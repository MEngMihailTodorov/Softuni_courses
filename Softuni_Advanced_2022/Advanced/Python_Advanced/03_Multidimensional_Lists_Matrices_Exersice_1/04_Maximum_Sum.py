n, m = map(int, input().split())
matrix = []
biggest_sum = -999999

for _ in range(n):
    matrix.append(list(map(int, input().split())))


for i in range(n - 2):
    for j in range(m - 2):
        sum = matrix[i][j] + matrix[i + 1][j] + matrix[i + 2][j] + \
              matrix[i][j + 1] + matrix[i + 1][j + 1] + matrix[i + 2][j + 1] + \
              matrix[i][j + 2] + matrix[i + 1][j + 2] + matrix[i + 2][j + 2]

        if sum > biggest_sum:
            saved_i = i
            saved_j = j
            biggest_sum = sum

print(f"Sum = {biggest_sum}")
for k in range(saved_i, saved_i + 3):
    print(f"{' '.join(str(matrix[k][l]) for l in range(saved_j, saved_j + 3))}")