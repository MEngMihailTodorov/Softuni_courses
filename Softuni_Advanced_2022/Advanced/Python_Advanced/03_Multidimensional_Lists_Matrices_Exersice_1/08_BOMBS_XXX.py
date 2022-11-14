# def explode_coordinate(n, matrix, coordinate):
#     coordinate = coordinate.split(",")
#
#     if 0 <= coordinate[0] < n and 0 <= coordinate[1] < n:
#         if matrix[int(coordinate[0])][int(coordinate[1])] > 0:
#             explosion = matrix[int(coordinate[0])][int(coordinate[1])]
#             matrix[int(coordinate[0])][int(coordinate[1])] = 0
#             if matrix[int(coordinate[0])][int(coordinate[1])]
#         else:
#             return matrix


n = int(input())
matrix = []
alive_number = 0
matrix_alive_sum = 0

for _ in range(n):
    matrix.append(list(map(int, input().split())))

coordinates = list(map(str, input().split()))

print(matrix)

for coordinate in coordinates:
    print(explode_coordinate(n, matrix, coordinate))
