def eat_cookies(presents_left, nice_kids):
    for coordinates in directions.values():
        r = santa_pos[0] + coordinates[0]
        c = santa_pos[1] + coordinates[1]

        if not presents_left:
            break

        if matrix[r][c].isalpha():
            if matrix[r][c] == "V":
                nice_kids += 1
            matrix[r][c] = "-"
            presents_left -= 1

    return presents_left, nice_kids


presents = int(input())
size = int(input())
matrix = [[str(i) for i in input().split()] for j in range(size)]

total_nice_kids = 0
nice_kids_visited = 0
santa_pos = []

# print(*matrix, sep="\n")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

for i in range(size):
    for j in range(size):
        if matrix[i][j] == "S":
            santa_pos = [i, j]
            matrix[i][j] = "-"
        elif matrix[i][j] == "V":
            total_nice_kids += 1

command = input()

while True:
    if command == "Christmas morning":
        break

    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1]
    ]

    house = matrix[santa_pos[0]][santa_pos[1]]

    if house == "V":
        nice_kids_visited += 1
        presents -= 1
    elif house == "C":
        presents, nice_kids_visited = eat_cookies(presents, nice_kids_visited)

    matrix[santa_pos[0]][santa_pos[1]] = "-"

    if not presents or nice_kids_visited == total_nice_kids:
        break

    command = input()

matrix[santa_pos[0]][santa_pos[1]] = "S"

if not presents and nice_kids_visited < total_nice_kids:
    print("Santa ran out of presents!")


print(*[" ".join(row) for row in matrix], sep="\n")

if nice_kids_visited == total_nice_kids:
    print(f"Good job, Santa! {nice_kids_visited} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_visited} nice kid/s.")