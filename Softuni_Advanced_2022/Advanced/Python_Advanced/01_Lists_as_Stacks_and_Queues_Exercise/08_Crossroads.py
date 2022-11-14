from collections import deque

original_green_light_window = int(input())
green_light_window = original_green_light_window
free_window_duration = int(input())
car_queue = deque()
total_cars_passed = 0
everyone_safe = True

while True:
    command = input()
    if command == "END":
        if everyone_safe:
            print("Everyone is safe.")
            print(f"{total_cars_passed} total cars passed the crossroads.")
        break

    elif command == "green":
        car_counter = 0

        for i in car_queue:
            green_light_window -= int(len(car_queue[car_counter]))

            if green_light_window <= 0:
                if green_light_window + free_window_duration < 0:
                    index = green_light_window + free_window_duration + len(i)
                    print("A crash happened!")
                    print(f"{i} was hit at {i[index]}.")
                    everyone_safe = False
                    break
                else:
                    car_counter += 1
                    break
            else:
                car_counter += 1
        for _ in range(car_counter):
            car_queue.popleft()

        total_cars_passed += car_counter
        green_light_window = original_green_light_window

    else:
        car = command
        car_queue.append(car)

    if not everyone_safe:
        break

