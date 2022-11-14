directions = {
    'up': lambda r, c: [r - 1, c],
    'down': lambda r, c: [r + 1, c],
    'right': lambda r, c: [r, c + 1],
    'left': lambda r, c: [r, c - 1],
}

matrix = []

start_row = 0
start_col = 0
targets_count = 0

killed_targets = []

for row in range(5):
    current_row = input().split()
    for col in range(5):
        if current_row[col] == 'A':
            start_row = row
            start_col = col
            current_row[col] = "."
        elif current_row[col] == 'x':
            targets_count += 1

    matrix.append(current_row)

n = int(input())
print(matrix)
for i in range(n):
    if targets_count == 0:
        print(f"Training completed! All {killed_targets} targets hit.")
        break

    command = input().split()

    action = command[0]
    direction = command[1]

    if action == 'move':
        steps_count = int(command[-1])
        for i in range(steps_count):
            next_row, next_col = directions[direction](start_row, start_col)

            if next_row < 0 or next_row >= 5 or next_col < 0 or next_col >= 5 or matrix[next_row][next_col] != '.':
                break

            matrix[start_row][start_col] = '.'
            start_row, start_col = next_row, next_col
    elif action == 'shoot':
        bullet_row, bullet_col = start_row, start_col
        while True:
            next_row, next_col = directions[direction](bullet_row, bullet_col)

            if next_row < 0 or next_row >= 5 or next_col < 0 or next_col >= 5:
                break

            if matrix[next_row][next_col] == 'x':
                matrix[next_row][next_col] = '.'
                targets_count -= 1
                killed_targets.append([next_row, next_col])
                break

            bullet_row, bullet_col = next_row, next_col


print(f"Training not completed! {targets_count} targets left.")

[print(x) for x in killed_targets]