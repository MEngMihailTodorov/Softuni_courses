from collections import deque

bees_queue = deque(map(int, input().split()))
nectar_stack = list(map(int, input().split()))

symbols = deque(map(str, input().split()))
total_honey = 0

while bees_queue and nectar_stack:

    if bees_queue[0] <= nectar_stack[-1]:
        symbol = symbols.popleft()
        collected_nectar, bee = nectar_stack.pop(), bees_queue.popleft()
        if symbol == "+":
            total_honey += abs(bee + collected_nectar)
        elif symbol == "-":
            total_honey += abs(bee - collected_nectar)
        elif symbol == "*":
            total_honey += abs(bee * collected_nectar)
        else:
            if collected_nectar == 0 or bee == 0:
                continue
            total_honey += abs(bee / collected_nectar)

    else:
        nectar_stack.pop()


print(f"Total honey made: {total_honey}")
if bees_queue:
    print(f"Bees left: {', '.join(map(str, bees_queue))}")

if nectar_stack:
    print(f"Nectar left: {', '.join(map(str, nectar_stack))}")