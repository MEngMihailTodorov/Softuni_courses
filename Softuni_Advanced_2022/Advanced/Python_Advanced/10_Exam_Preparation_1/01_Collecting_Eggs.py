from collections import deque

eggs_queue = deque(map(int, input().split(", ")))
paper_stack = list(map(int, input().split(", ")))
total_boxes = 0

while eggs_queue and paper_stack:
    current_egg = eggs_queue.popleft()
    if current_egg <= 0:
        pass
    elif current_egg == 13:
        paper_stack.insert(0, paper_stack.pop())
        paper_stack.append(paper_stack.pop(1))
    else:
        current_paper = paper_stack.pop()
        if current_paper + current_egg <= 50:
            total_boxes += 1
        else:
            pass

if total_boxes > 0:
    print(f"Great! You filled {total_boxes} boxes.")
    if paper_stack:
        print(f"Pieces of paper left: {', '.join([str(i) for i in paper_stack])}")
    if eggs_queue:
        print(f"Eggs left: {', '.join([str(i) for i in eggs_queue])}")
else:
    print(f"Sorry! You couldn't fill any boxes!")
    if paper_stack:
        print(f"Pieces of paper left: {', '.join([str(i) for i in paper_stack])}")
    if eggs_queue:
        print(f"Eggs left: {', '.join([str(i) for i in eggs_queue])}")