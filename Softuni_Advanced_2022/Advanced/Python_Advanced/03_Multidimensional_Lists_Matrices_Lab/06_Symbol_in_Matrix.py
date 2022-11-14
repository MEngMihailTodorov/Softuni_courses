n = int(input())
matrix = []

for i in range(n):
    matrix.append([str(i) for substring in input() for i in substring])

symbol = str(input())
exists = False

for i in range(n):
    for j in range(n):
        if matrix[i][j] == symbol:
            exists = True
            break
    if exists:
        break


if exists:
    print((i, j))
else:
    print(f"{symbol} does not occur in the matrix")