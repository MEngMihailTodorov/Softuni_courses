def move(direction, new_position):
    new_pos = [directions[direction][0] + new_position[0], new_position[1] + directions[direction][1]]
    return new_pos


n = int(input())
matrix = [[i for i in input().split()] for _ in range(n)]
bunny_coordinates = []
max_eggs_collected = 0
max_eggs_direction = 0
max_collected_points = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

for i in range(n):
    for j in range(n):
        if matrix[i][j] == "B":
            bunny_coordinates = [i, j]


for direction in directions.keys():
    current_eggs = 0
    new_position = bunny_coordinates.copy()
    new_position = move(direction, new_position)
    collected_points = []
    while 0 <= new_position[0] < n and 0 <= new_position[1] < n:

        if matrix[new_position[0]][new_position[1]] == "X":
            break
        else:
            current_eggs += int(matrix[new_position[0]][new_position[1]])
            collected_points.append([new_position[0], new_position[1]])
        new_position = move(direction, new_position)

    if current_eggs > max_eggs_collected:
        max_eggs_direction = direction
        max_eggs_collected = current_eggs
        max_collected_points = collected_points


print(max_eggs_direction)
for point in max_collected_points:
    print(point)
print(max_eggs_collected)
