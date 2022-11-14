def rectangle(a, b):
    if type(a) == int and type(b) == int:
        return area(a, b) + "\n" + perimeter(a, b)
    return "Enter valid values!"


def area(a, b):
    return f"Rectangle area: {a * b}"


def perimeter(a, b):
    return f"Rectangle perimeter: {2 * (a + b)}"


print(rectangle(2, 10))