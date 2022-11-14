from collections import deque
n = int(input())
stops = 0
total_fuel = 0
q = deque()


for i in range(n):
    q.append(input())

length = len(q)
stops = 0
original_1 = q.copy()


while stops != length:
    fuel, distance = q[0].split(" ")
    total_fuel += int(fuel)
    distance = int(distance)

    if total_fuel >= distance:
        el = q.popleft()
        total_fuel -= int(el.split()[1])
        q.append(el)
        stops += 1
    else:
        stops = 0
        q.append(q.popleft())
        total_fuel = 0

print(original_1.index((q[0])))
