n, m = map(int, input().split())
matrix = []

for i in range(n):
    matrix.append([])
    for j in range(m):
        element_list = [chr(97 + i), chr(97 + j + i), chr(97 + i)]
        element = ''.join(element_list)
        matrix[i].append(element)

for k in range(n):
    print(f"{' '.join(str(matrix[k][l]) for l in range(m))}")