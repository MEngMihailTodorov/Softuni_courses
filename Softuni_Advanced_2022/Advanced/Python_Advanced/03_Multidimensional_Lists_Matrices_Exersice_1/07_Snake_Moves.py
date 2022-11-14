from collections import deque

n, m = map(int, input().split())
word_queue = deque(input())
matrix = []

for i in range(n):
    matrix.append([])
    if i % 2 == 0:
        for j in range(m):
            element = word_queue.popleft()
            matrix[i].append(element)
            word_queue.append(element)
    else:
        for j in range(m):
            element = word_queue.popleft()
            matrix[i].insert(0, element)
            word_queue.append(element)

for k in range(n):
    print(f"{''.join(str(matrix[k][l]) for l in range(m))}")