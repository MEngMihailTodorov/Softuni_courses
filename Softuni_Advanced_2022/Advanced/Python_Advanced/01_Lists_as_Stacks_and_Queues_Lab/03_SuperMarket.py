queue = []

while True:
    current_command = input()
    if current_command == "End":
        print(f"{len(queue)} people remaining.")
        break
    elif current_command == "Paid":
        for i in queue:
            print(i)
        queue = []
    else:
        queue.append(current_command)