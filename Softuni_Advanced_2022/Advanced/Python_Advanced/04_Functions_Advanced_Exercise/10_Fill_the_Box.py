def fill_the_box(height: int, length: int, width: int, *args):
    space = height * length * width
    remaining_space = space
    cubes = 0
    cubes_slots = 0

    for el in args:
        if el == "Finish":
            break
        else:
            cubes += int(el)
            cubes_slots += 1

    for el in range(cubes_slots):
        remaining_space -= int(args[el])
        if remaining_space <= 0:
            return f"No more free space! You have {cubes - space} more cubes."

    return f"There is free space in the box. You could put {remaining_space} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))