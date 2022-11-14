from collections import deque

cup_capacity = deque(map(int, input().split()))
bottle_capacity = list(map(int, input().split()))

wasted_water = 0


while cup_capacity and bottle_capacity:
    water_remaining = bottle_capacity.pop()

    if cup_capacity[0] <= water_remaining:
        wasted_water += water_remaining - cup_capacity.popleft()


    else:
        cup_capacity[0] -= water_remaining


if cup_capacity:
    result = ""
    for i in cup_capacity:
        result += str(i)
        result += " "

    result = result[:(len(result)- 1):]

    print(f"Cups: {result}")
    print(f"Wasted litters of water: {wasted_water}")
else:
    result = ""
    for i in bottle_capacity:
        result += str(i)
        result += " "

    result = result[:(len(result) - 1):]

    print(f"Bottles: {result}")
    print(f"Wasted litters of water: {wasted_water}")