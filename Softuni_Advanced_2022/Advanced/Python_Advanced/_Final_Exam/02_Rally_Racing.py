n = int(input())

tracked_race_car = input()
car_pos = [0, 0]
matrix = [[x for x in input().split()] for _ in range(n)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)

}

distance_travelled = 0

tunnel_pos = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'T':
            tunnel_pos.append([i, j])

# print(*[" ".join(row) for row in matrix], sep="\n")
# print(tunnel_pos)


while True:
    current_command = input()

    if current_command == "End":
        matrix[car_pos[0]][car_pos[1]] = "C"
        print(f"Racing car {tracked_race_car} DNF.")
        print(f"Distance covered {distance_travelled} km.")
        print(*["".join(row) for row in matrix], sep="\n")
        break

    if matrix[car_pos[0]][car_pos[1]] == "F":
        matrix[car_pos[0]][car_pos[1]] = "C"
        print(f"Racing car {tracked_race_car} finished the stage!")
        print(f"Distance covered {distance_travelled} km.")
        print(*["".join(row) for row in matrix], sep="\n")
        break

    car_pos[0] = car_pos[0] + directions[current_command][0]
    car_pos[1] = car_pos[1] + directions[current_command][1]

    if matrix[car_pos[0]][car_pos[1]] == "T":
        matrix[car_pos[0]][car_pos[1]] = '.'
        car_pos[0] = tunnel_pos[1][0]
        car_pos[1] = tunnel_pos[1][1]
        matrix[car_pos[0]][car_pos[1]] = '.'
        distance_travelled += 30
    else:
        distance_travelled += 10