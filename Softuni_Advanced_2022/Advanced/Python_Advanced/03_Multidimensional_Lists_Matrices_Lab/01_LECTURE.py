# matrix = []  # n x m matrix [n][m]
#
# for i in range(3):
#     matrix.append([])
#     for j in range(4):
#         matrix[i].append(input())
#
# print(matrix)
#
#
# matrix2 = []
#
# for _ in range(5):
#     matrix2.append([])
#
# print(matrix2)

rows, cols = [int(x) for x in input().split(", ")]

print(rows, cols)

matrix3 = []

for _ in range(rows):
    matrix3.append([int(x) for x in input().split(", ")])

print(matrix3)

# nested comprehension
