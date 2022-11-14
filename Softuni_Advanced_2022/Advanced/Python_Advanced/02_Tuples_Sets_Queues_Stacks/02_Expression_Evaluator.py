# import math
#
# string = list(map(str, input().split()))
# total_list = []
# total_sum = 0
#
# for i in string:
#     if i.isdigit():
#         total_list.append(int(i))
#     elif i[0] == "-" and len(i) > 1:
#         total_list.append(-int(i[1]))
#     elif i == "+":
#         total_sum = sum(total_list)
#         total_list = [total_sum]
#     elif i == "-":
#         total_sum = total_list[0] - sum([i for i in total_list[1::]])
#         total_list = [total_sum]
#     elif i == "/":
#         total_sum = total_list[0]
#         for i in total_list[1::]:
#             total_sum = total_sum / i
#
#         total_sum = math.floor(total_sum)
#         total_list = [total_sum]
#
#     elif i == "*":
#         total_sum = total_list[0]
#         for j in total_list[1::]:
#             total_sum *= j
#
#         total_sum = math.floor(total_sum)
#         total_list = [total_sum]
#
# print(total_sum)


from functools import reduce
import math

expression = input().split()
stack = []

for item in expression:
    if item.lstrip('-').isnumeric():
        stack.append(int(item))
    else:
        if item == "*":
            stack = [reduce(lambda x, y: x * y, stack)]
        elif item == "/":
            stack = [reduce(lambda x, y: math.floor(x / y), stack)]
        elif item == "+":
            stack = [reduce(lambda x, y: x + y, stack)]
        elif item == "-":
            stack = [reduce(lambda x, y: x - y, stack)]

print(stack[0])