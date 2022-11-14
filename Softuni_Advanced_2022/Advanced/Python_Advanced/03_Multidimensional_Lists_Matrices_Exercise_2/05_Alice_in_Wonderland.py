def move(direction):
    new_pos = [directions[direction][0] + alice_position[0], alice_position[1] + directions[direction][1]]
    return new_pos


n = int(input())
matrix = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)

}
alice_position = []
tea_bags = 0
alice_did_not_make_it = False

for i in range(n):
    line = list(input().split())

    matrix.append(line)

    if "A" in line:
        alice_position = [i, line.index("A")]
        matrix[alice_position[0]][alice_position[1]] = "*"


while tea_bags < 10:
    direction = input()
    new_position = move(direction)

    if 0 <= new_position[0] < n and 0 <= new_position[1] < n:
        if matrix[new_position[0]][new_position[1]].isnumeric():
            tea_bags += int(matrix[new_position[0]][new_position[1]])
            alice_position = [new_position[0], new_position[1]]
            matrix[new_position[0]][new_position[1]] = "*"

        elif matrix[new_position[0]][new_position[1]] == "R":
            alice_did_not_make_it = True
            break

        else:
            alice_position = [new_position[0], new_position[1]]
            matrix[new_position[0]][new_position[1]] = "*"
    else:
        alice_did_not_make_it = True
        break

if alice_did_not_make_it:
    print(f"Alice didn't make it to the tea party.")
else:
    print(f"She did it! She went to the party.")

print(*[" ".join(row) for row in matrix], sep="\n")