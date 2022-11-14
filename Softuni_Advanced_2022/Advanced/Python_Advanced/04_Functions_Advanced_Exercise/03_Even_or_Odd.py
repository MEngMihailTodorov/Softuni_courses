def even_odd(*args):
    result = []
    if args[-1] == "even":
        args = args[0:len(args)-1:1]
        for el in args:
            if el % 2 == 0:
                result.append(el)

    elif args[-1] == "odd":
        args = args[0:len(args) - 1:1]
        for el in args:
            if el % 2 == 1:
                result.append(el)

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))