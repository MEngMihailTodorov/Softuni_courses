n = int(input())
matrix = [[str(i) for i in input()] for _ in range(n)]
removed_knights = 0
positions = (
    (-2, 1),
    (-2, -1),
    (-1, -2),
    (-1, 2),
    (1, 2),
    (1, -2),
    (2, 1),
    (2, -1),
)


while True:
    max_attack = 0
    knight_max_attack_position = []

    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "K":
                attacks = 0
                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < n and 0 <= pos_col < n:
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1

                if attacks > max_attack:
                    max_attack = attacks
                    knight_max_attack_position = [row, col]

    if knight_max_attack_position:
        matrix[knight_max_attack_position[0]][knight_max_attack_position[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)