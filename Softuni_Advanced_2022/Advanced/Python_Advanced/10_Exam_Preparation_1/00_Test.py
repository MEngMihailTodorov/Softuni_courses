
n = 6
matrix = []

for i in range(n):
    matrix.append([' '.join(str(i) for i in input().split())])


print(matrix[2])