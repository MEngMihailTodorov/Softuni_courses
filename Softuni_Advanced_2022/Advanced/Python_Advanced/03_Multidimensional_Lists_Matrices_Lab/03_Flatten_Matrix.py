n_rows = int(input())
matrix = []

for i in range(n_rows):
    matrix.append([int(i) for i in input().split(", ")])

flattened_matrix = [num for substring in matrix for num in substring]

print(flattened_matrix)