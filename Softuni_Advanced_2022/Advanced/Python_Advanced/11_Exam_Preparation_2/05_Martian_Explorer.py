SIZE = 6
matrix = []
rover_pos = []

for row in range(SIZE):
    line = input().split()

    if 'E' in line:
        rover_pos = [row, line.index('E')]

    matrix.append(line)

commands = input().split(", ")

deposits = {
    'W': 0,
    'M': 0,
    'C': 0
}

deposits_names = {
    'W': 'Water',
    'M': 'Metal',
    'C': 'Concrete',
}
directions = {
    'right': [0, 1],
    'left': [0, -1],
    'up': [-1, 0],
    'down': [1, 0],
}

while commands:
    command = commands.pop(0)

    rover_pos[0] = (rover_pos[0] + directions[command][0])
    rover_pos[1] = (rover_pos[1] + directions[command][1])

    for i in range(len(rover_pos)):
        if rover_pos[i] < 0:
            rover_pos[i] = SIZE - 1
        elif rover_pos[i] == SIZE:
            rover_pos[i] = 0

    position = matrix[rover_pos[0]][rover_pos[1]]

    if position == "W" or position == "M" or position == "C":
        deposits[position] += 1
        print(f"{deposits_names[position]} deposit found at ({rover_pos[0]}, {rover_pos[1]})")

    elif position == "R":
        print(f"Rover got broken at ({rover_pos[0]}, {rover_pos[1]})")
        break

area_suitable = True

for j in deposits.values():
    if j == 0:
        area_suitable = False
    else:
        pass

if area_suitable:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

