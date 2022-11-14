# def operate(operator, *args):
#     if operator == "+":
#         result = 0
#         for el in args:
#             result += int(el)
#         return result
#     elif operator == "*":
#         result = 1
#         for el in args:
#             result *= int(el)
#         return result
#     elif operator == "-":
#         result = args[0]
#         for el in args[1::]:
#             result -= int(el)
#         return result
#     elif operator == "/":
#         result = [0]
#         for el in args[1::]:
#             if int(el) == 0:
#                 pass
#             else:
#                 result += int(el)
#         return result
#
#
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))

def operate(operator, *args):
    def add():
        return sum(args)

    def multiply():
        result = 1
        for el in args:
            result *= el
        return result

    def subtract():
        result = args[0]
        for i in args[1::]:
            result -= i
        return result

    def divide():
        result = args[0]
        for i in args[1::]:
            result = result/i
        return result

    if operator == "+":
        return add()
    elif operator == "*":
        return multiply()
    elif operator == "/":
        return divide()
    elif operator == "-":
        return subtract()