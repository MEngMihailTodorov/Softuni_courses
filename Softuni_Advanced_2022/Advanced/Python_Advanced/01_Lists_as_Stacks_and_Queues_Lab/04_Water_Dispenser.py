n = int(input())
queue = []

while True:
    current_name = input()

    if current_name == "Start":
        break

    queue.append(current_name)

counter = 0

while True:
    current_command = input()

    if current_command == "End":
        print(f"{n} liters left")
        break

    elif current_command.isdigit():
        n -= int(current_command)
        if n < 0:
            print(f"{queue[counter]} must wait")
            n += int(current_command)
        else:
            print(f"{queue[counter]} got water")
        counter += 1

    else:
        n += int(current_command.split()[1])
