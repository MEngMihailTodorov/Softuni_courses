n = int(input())
lst = list(map(int, input().split()))
max_order = max(lst)

for i in range(len(lst)):
    n -= lst[i]

    if n < 0:
        print(max_order)
        print(f"Orders left: {' '.join([str(j) for j in lst[i:len(lst):1]])}")
        break
    elif i == len(lst) - 1:
        print(max_order)
        print(f"Orders complete")
        break
    else:
        pass
