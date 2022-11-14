import triangle as tr

n= int(input())

for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(col, end=' ')
    print()

for r in range(n-1, 0, -1):
    for c in range(1, r + 1):
        print(c, end=' ')
    print()

print(tr.triangle_function(n))