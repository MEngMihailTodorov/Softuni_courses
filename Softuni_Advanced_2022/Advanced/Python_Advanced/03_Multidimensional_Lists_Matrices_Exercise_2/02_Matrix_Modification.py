n = int(input())

matrix = [[int(i) for i in input().split()] for _ in range(n)]

while True:
    command = input().split()

    if command[0] == "END":
        break

    if command[0] == 'Add':
        if 0 <= int(command[1]) < n and 0 <= int(command[2]) < n:
            matrix[int(command[1])][int(command[2])] += int(command[3])
        else:
            print(f"Invalid coordinates")

    elif command[0] == "Subtract":
        if 0 <= int(command[1]) < n and 0 <= int(command[2]) < n:
            matrix[int(command[1])][int(command[2])] -= int(command[3])
        else:
            print(f"Invalid coordinates")


for i in range(n):
    print(" ".join(str(j) for j in matrix[i]))