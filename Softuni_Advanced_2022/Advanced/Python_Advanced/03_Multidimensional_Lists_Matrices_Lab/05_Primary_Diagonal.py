n_rows = int(input())
matrix = []
sum_diagonal = 0

for i in range(n_rows):
    matrix.append([int(i) for i in input().split()])

for i in range(n_rows):
    sum_diagonal += matrix[i][i]

print(sum_diagonal)