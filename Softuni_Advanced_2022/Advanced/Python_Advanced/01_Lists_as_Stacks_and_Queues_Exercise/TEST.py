# from collections import deque
# n = int(input())
# stops = 0
# total_fuel = 0
# q = deque()
#
#
# for i in range(n):
#     q.append(input())
#
# length = len(q)
# stops = 0
# original_1 = q.copy()
# print(q)
#
#
# print(q[0])
# el, el2 = q[0].split()
# print(el, el2)
#
# q.append(q.popleft())
# print(q)


def turn_to_time(n):
    seconds = n % 60 % 60
    minutes = (n - seconds) // (60)
    hours = minutes // 60
    minutes = minutes % 60
    return f"[{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}]"


print(turn_to_time(4000))


# import time
#
# # seconds passed since epoch
# seconds = 28800
# local_time = time.ctime(seconds)
# print("Local time:", local_time)