n = int(input())
n_set = set()

for i in range(n):
    current_command = tuple(input().split())
    for j in current_command:
        n_set.add(j)

for el in n_set:
    print(el)