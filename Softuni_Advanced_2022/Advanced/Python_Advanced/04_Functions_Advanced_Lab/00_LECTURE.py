a = [1, 2, 5, 6, 2, 3, 4]

a.sort()

print(a)


people = {
    "ivan": 14,
    "gosho": 23,
    "mimi": 14,
    "ani": 14,
}

result = sorted(people.keys(), key=lambda x: (len(x), x))
print(result)
print(len(people))


def my_func(operator):
    def my_func2(*args):
        return "mega cool"
    if operator == "+":
        return my_func2()
    else:
        return "ne e mega cool"


print(my_func("-"))