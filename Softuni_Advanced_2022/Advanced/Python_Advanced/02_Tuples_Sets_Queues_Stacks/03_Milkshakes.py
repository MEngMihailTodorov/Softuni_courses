# from collections import deque
#
# chocolate_stack = list(map(int, input().split(', ')))
# milk_queue = deque(map(int, input().split(', ')))
# milk_shakes_made = 0
#
# while chocolate_stack:
#     if chocolate_stack[-1] <= 0:
#         chocolate_stack.pop()
#     if milk_queue[0] <= 0:
#         milk_queue.popleft()
#
#     if len(milk_queue) == 0 or chocolate_stack == 0:
#         print("Not enough milkshakes.")
#         if chocolate_stack:
#             print(f"Chocolate: {', '.join(str(i) for i in chocolate_stack)}")
#         else:
#             print(f"Chocolate: empty")
#         if milk_queue:
#             print(f"Milk: {', '.join(str(i) for i in milk_queue)}")
#         else:
#             print(f"Milk: empty")
#         break
#
#     if chocolate_stack[-1] == milk_queue[0]:
#         chocolate_stack.pop()
#         milk_queue.popleft()
#
#         milk_shakes_made += 1
#
#         if milk_shakes_made == 5:
#             print("Great! You made all the chocolate milkshakes needed!")
#             if chocolate_stack:
#                 print(f"Chocolate: {', '.join(str(i) for i in chocolate_stack)}")
#             else:
#                 print(f"Chocolate: empty")
#             if milk_queue:
#                 print(f"Milk: {', '.join(str(i) for i in milk_queue)}")
#             else:
#                 print(f"Milk: empty")
#             break
#     else:
#         milk_queue.append(milk_queue.popleft())
#         chocolate_stack[-1] -= 5
#
#     if len(milk_queue) == 0 or chocolate_stack == 0:
#         print("Not enough milkshakes.")
#         if chocolate_stack:
#             print(f"Chocolate: {', '.join(str(i) for i in chocolate_stack)}")
#         else:
#             print(f"Chocolate: empty")
#         if milk_queue:
#             print(f"Milk: {', '.join(str(i) for i in milk_queue)}")
#         else:
#             print(f"Milk: empty")
#         break


from collections import deque

chocolate_stack = list(map(int, input().split(', ')))
milk_queue = deque(map(int, input().split(', ')))
milk_shakes_made = 0


while milk_shakes_made < 5 and chocolate_stack and milk_queue:
    flag = False
    if chocolate_stack[-1] <= 0:
        chocolate_stack.pop()
        flag = True

    if milk_queue[0] <= 0:
        milk_queue.popleft()
        flag = True

    if flag:
        continue

    if chocolate_stack[-1] == milk_queue[0]:
        milk_shakes_made += 1
        chocolate_stack.pop()
        milk_queue.popleft()
    else:
        milk_queue.append(milk_queue.popleft())
        chocolate_stack[-1] -= 5

if milk_shakes_made == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate_stack:
    print(f"Chocolate: {', '.join(str(i) for i in chocolate_stack)}")
else:
    print(f"Chocolate: empty")
if milk_queue:
    print(f"Milk: {', '.join(str(i) for i in milk_queue)}")
else:
    print(f"Milk: empty")
