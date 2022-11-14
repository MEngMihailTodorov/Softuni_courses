from collections import deque


def turn_to_time(n):
    seconds = n % 60 % 60
    minutes = (n - seconds) // (60)
    hours = minutes // 60
    minutes = minutes % 60
    return f"[{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}]"


robots = deque(map(str, input().split(";")))
start_time = list(map(int, input().split(":")))
start_time = 60 * 60 * start_time[0] + 60 * start_time[1] + start_time[2]
original_robots = robots.copy()


product_queue = deque()

while True:
    product = input()
    if product == "End":
        break
    else:
        product_queue.append(product)

time_tracker = 1
print(product_queue)
print(robots)
robots_dict = {}

for robot in robots:
    robot = robot.split('-')
    d = {robot[0]: int(robot[1])}
    robots_dict.update(d)

robots_original_dict = robots_dict.copy()

print(robots_dict)

while product_queue:
    if robots:
        product = product_queue.popleft()
        robot = robots.popleft()
        print(f"{robot.split('-')[0]} - {product} {turn_to_time(time_tracker + start_time)}")
    else:
        product_queue.append(product_queue.popleft())
        pass

    for i in robots_dict.keys():
        if robots_dict[i] == 0:
            robots.append()


    time_tracker += 1
