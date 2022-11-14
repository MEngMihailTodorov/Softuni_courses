n = int(input())

stack = []
for i in range(n):
    current_input = input()

    if str(current_input) == "2":
        if len(stack) == 0:
            pass
        else:
            stack.pop(len(stack) - 1)
    elif str(current_input) == "3":
        if len(stack) == 0:
            pass
        else:
            print(max(stack))
    elif str(current_input) == "4":
        if len(stack) == 0:
            pass
        else:
            print(min(stack))
    else:
        number = list(map(int, current_input.split(" ")))
        number = number[1]
        stack.append(number)


print(", ".join([str(j) for j in stack[::-1]]))