kids = list(map(str, input().split()))
n = int(input())
start_index = 0

while True:
    if len(kids) == 1:
        print(f"Last is {kids[0]}")
        break
    else:
        index = (n + start_index - 1) % len(kids)
        print(f"Removed {kids.pop(index)}")
        start_index = index