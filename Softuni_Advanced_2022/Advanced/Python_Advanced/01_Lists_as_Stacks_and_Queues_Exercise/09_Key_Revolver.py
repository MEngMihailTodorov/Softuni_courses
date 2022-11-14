from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullet_list = list(map(int, input().split()))
locks_queue = deque(map(int, input().split()))
intelligence_value = int(input())

total_bullets_used = 0
bullets_present = gun_barrel_size
breaking_point = False

while locks_queue:

    if not bullet_list:
        print(f"Couldn't get through. Locks left: {len(locks_queue)} ")
        breaking_point = True
        break

    if bullets_present == 0:
        print(f"Reloading!")
        bullets_present = gun_barrel_size

    if bullet_list:
        bullet_power = bullet_list.pop()

        if bullet_power <= locks_queue[0]:
            locks_queue.popleft()
            print("Bang!")
        else:
            print("Ping!")

        bullets_present -= 1
        total_bullets_used += 1


if not breaking_point:
    bullets_left = len(bullet_list)

    if bullets_present == 0 and bullets_left != 0:
        print(f"Reloading!")
        bullets_present = gun_barrel_size

    print(f"{bullets_left} bullets left. Earned ${intelligence_value - total_bullets_used * bullet_price}")
else:
    pass
