expression = input()
stack = []

for i in range(len(expression)):
    if expression[i] == "(":
        stack.append(i)
    elif expression[i] == ")":
        last = stack.pop()
        print(expression[last:i+1:1])
    else:
        pass