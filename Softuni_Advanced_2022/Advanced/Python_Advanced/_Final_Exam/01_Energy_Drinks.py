from collections import deque

initial_caffeine = 0
max_caffeine = 300


milligrams_stack = list(map(int, input().split(", ")))
drinks_queue = deque(map(int, input().split(", ")))


while milligrams_stack and drinks_queue:
    new_drinks = drinks_queue.popleft()
    new_amount = milligrams_stack.pop() * new_drinks

    if initial_caffeine + new_amount > max_caffeine:
        initial_caffeine -= 30
        if initial_caffeine < 0:
            initial_caffeine = 0
        drinks_queue.append(new_drinks)
    else:
        initial_caffeine += new_amount


if drinks_queue:
    print(f"Drinks left: {', '.join(str(x) for x in drinks_queue)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {initial_caffeine} mg caffeine.")