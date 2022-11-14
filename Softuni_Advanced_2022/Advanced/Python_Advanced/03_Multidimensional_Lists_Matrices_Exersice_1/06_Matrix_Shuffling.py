n, m = map(int, input().split())
matrix = []

for _ in range(n):
    matrix.append(list(map(str, input().split())))


while True:
    command = list(map(str, input().split()))

    if command[0] == "END":
        break
    elif command[0] == "swap" and len(command) == 5:
        if 0 <= int(command[1]) < n and 0 <= int(command[2]) < m and 0 <= int(command[3]) < n and 0 <= int(command[4]) < m:
            matrix[int(command[1])][int(command[2])], matrix[int(command[3])][int(command[4])] =\
                matrix[int(command[3])][int(command[4])], matrix[int(command[1])][int(command[2])]
            for a in range(n):
                print(f"{' '.join(str(matrix[a][b]) for b in range(m))}")

        else:
            print(f"Invalid input!")
            pass
    else:
        print(f"Invalid input!")
        pass
