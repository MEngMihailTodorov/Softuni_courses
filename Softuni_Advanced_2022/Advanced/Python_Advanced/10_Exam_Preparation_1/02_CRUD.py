# Create, Read, Update, Delete

n = 6

matrix = [[str(i) for i in input().split()] for _ in range(n)]

start_position = input()
start_row = int(start_position[1])
start_col = int(start_position[4])

directions = {
    'right': [0, 1],
    'left': [0, -1],
    'up': [-1, 0],
    'down': [1, 0],
}

command = list(map(str, input().split(", ")))

while command[0] != "Stop":

    if command[0] == 'Create':
        direction = command[1]
        value = command[2]
        if 0 <= (start_row + int(directions[direction][0])) < 6 and 0 <= (start_col + int(directions[direction][1])) < 6:
            start_row = int(start_row + int(directions[direction][0]))
            start_col = int(start_col + int(directions[direction][1]))

            if matrix[start_row][start_col] == ".":
                matrix[start_row][start_col] = value
            else:
                pass
        else:
            pass

    elif command[0] == 'Update':
        direction = command[1]
        value = command[2]
        if 0 <= (start_row + directions[direction][0]) < 6 and 0 <= (start_col + directions[direction][1]) < 6:
            start_row = int(start_row + int(directions[direction][0]))
            start_col = int(start_col + int(directions[direction][1]))

            if matrix[start_row][start_col] != ".":
                matrix[start_row][start_col] = value
            else:
                pass
        else:
            pass

    elif command[0] == 'Delete':
        direction = command[1]
        if 0 <= (start_row + directions[direction][0]) < 6 and 0 <= (start_col + directions[direction][1]) < 6:
            start_row = int(start_row + int(directions[direction][0]))
            start_col = int(start_col + int(directions[direction][1]))

            if matrix[start_row][start_col] != ".":
                matrix[start_row][start_col] = "."
            else:
                pass
        else:
            pass

    elif command[0] == 'Read':
        direction = command[1]
        if 0 <= (start_row + directions[direction][0]) < 6 and 0 <= (start_col + directions[direction][1]) < 6:
            start_row = int(start_row + int(directions[direction][0]))
            start_col = int(start_col + int(directions[direction][1]))

            if matrix[start_row][start_col] != ".":
                print(matrix[start_row][start_col])
            else:
                pass
        else:
            pass

    command = list(map(str, input().split(", ")))

for i in range(n):
    print(" ".join(str(j) for j in matrix[i]))
