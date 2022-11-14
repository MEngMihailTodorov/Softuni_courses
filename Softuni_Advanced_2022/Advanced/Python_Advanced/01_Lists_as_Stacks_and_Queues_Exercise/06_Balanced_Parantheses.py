# def balanced(str):
#     if str[0] not in "({[":
#         return "NO"
#
#     counter_1 = 0
#     counter_2 = 0
#     counter_3 = 0
#
#     for i in str:
#         if i == "(":
#             counter_1 += 1
#         elif i == "{":
#             counter_2 += 1
#         elif i == "[":
#             counter_3 += 1
#         elif i == ")":
#             counter_1 -= 1
#         elif i == "}":
#             counter_2 -= 1
#         elif i == "]":
#             counter_3 -= 1


# Python3 code to Check for
# balanced parentheses in an expression
open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


# Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


# Driver code
string = input()
print(check(string))