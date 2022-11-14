# 1 ^ 0 = 1
# 0 ^ 1 = 1
# 0 ^ 0 = 0
a = 5
b = 4
print(~a)

# 000....000
# -2^31 -> 2^31 - 1
#  ~000...001 = 1
# =111....1110 = -2
# 0111...11111 = (2^31 - 1)
# (2^31 - 1) + 1 = 1000.00000 = -2^31
#
print(~1)

# array with n * 2 - 1 elements n different n - 1 of them are seen twice on of them is seen once
# find out with one with only one for cycle
a = [1, 2, 3, 1, 2]
lentgth = len(a)
# 1 ^ 1 = 0
# 2 ^ 2 = 0
# 0 ^ 3 = 3
# 000...000
# 000...011
# = 000....0011
result = 0
for i in range(lentgth):
    result ^= a[i]

print(result)


# -x = ~x + 1
