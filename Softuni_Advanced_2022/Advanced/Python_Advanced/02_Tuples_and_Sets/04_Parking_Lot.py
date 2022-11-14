n = int(input())
cars = set()

for i in range(n):
    direction, number = input().split(", ")

    if direction == "IN":
        cars.add(number)
    else:
        if number in cars:
            cars.remove(number)
        else:
            pass

if cars:
    for j in cars:
        print(j)
else:
    print("Parking Lot is Empty")