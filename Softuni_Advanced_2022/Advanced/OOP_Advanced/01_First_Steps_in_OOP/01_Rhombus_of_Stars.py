def star_rhombus(n):
    output = ''
    for row in range(1, n + 1):
        output += ' ' * (n - row)
        for col in range(1, row + 1):
            output += "* "
        output += "\n"

    for row in range(n - 1, 0, -1):
        output += ' ' * (n - row)
        for col in range(row + 1, 1, -1):
            output += "* "
        output += "\n"

    return output


n = int(input())
print(star_rhombus(n))
