from collections import deque

seat_matches_list = list(map(str, input().split(", ")))
numbers_queue = deque(map(int, input().split(", ")))
numbers_stack = list(map(int, input().split(", ")))

rotations = 0
matches = 0
matches_list = []

while matches < 3 and rotations < 10:
    number_1 = numbers_queue.popleft()
    number_2 = numbers_stack.pop()

    seas_1 = str(number_1) + chr(number_2 + number_1)
    seas_2 = str(number_2) + chr(number_2 + number_1)

    if seas_1 in seat_matches_list:
        matches_list.append(seat_matches_list.pop(seat_matches_list.index(seas_1)))
        rotations += 1
        matches += 1
    elif seas_2 in seat_matches_list:
        matches_list.append(seat_matches_list.pop(seat_matches_list.index(seas_2)))
        rotations += 1
        matches += 1
    else:
        rotations += 1
        numbers_queue.append(number_1)
        numbers_stack.insert(0, number_2)

print(f"Seat matches: {', '.join(str(i) for i in matches_list)}")
print(f"Rotations count: {rotations}")