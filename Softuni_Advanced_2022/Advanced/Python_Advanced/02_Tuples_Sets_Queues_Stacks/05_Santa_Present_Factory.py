from collections import deque

crafting_materials_stack = list(map(int, input().split()))
magic_level = deque(map(int, input().split()))

item_dict = {
    "Doll": {"magic": 150, "crafted": 0},
    "Wooden train": {"magic": 250, "crafted": 0},
    "Teddy bear": {"magic": 300, "crafted": 0},
    "Bicycle": {"magic": 400, "crafted": 0}
             }

while crafting_materials_stack and magic_level:

    product = crafting_materials_stack[-1] * magic_level[0]

    if crafting_materials_stack[-1] == 0:
        crafting_materials_stack.pop()
        flag = True

    if magic_level[0] == 0:
        magic_level.popleft()
        flag = True

    if product == item_dict["Doll"]["magic"]:
        item_dict["Doll"]["crafted"] += 1
        crafting_materials_stack.pop()
        magic_level.popleft()

    elif product == item_dict["Wooden train"]["magic"]:
        item_dict["Wooden train"]["crafted"] += 1
        crafting_materials_stack.pop()
        magic_level.popleft()

    elif product == item_dict["Teddy bear"]["magic"]:
        item_dict["Teddy bear"]["crafted"] += 1
        crafting_materials_stack.pop()
        magic_level.popleft()

    elif product == item_dict["Bicycle"]["magic"]:
        item_dict["Bicycle"]["crafted"] += 1
        crafting_materials_stack.pop()
        magic_level.popleft()

    else:
        if product > 0:
            crafting_materials_stack[-1] += 15
            magic_level.popleft()
        elif product < 0:
            crafting_materials_stack.append(crafting_materials_stack.pop() + magic_level.popleft())

if item_dict["Doll"]["crafted"] > 0 and item_dict["Wooden train"]["crafted"] > 0 or item_dict["Teddy bear"]["crafted"] \
        and item_dict["Bicycle"]["crafted"]:

    print("The presents are crafted! Merry Christmas!")

else:
    print("No presents this Christmas!")


if crafting_materials_stack:
    print(f"Materials left: {', '.join(str(crafting_materials_stack[i]) for i in range(-1, -len(crafting_materials_stack) - 1, -1))}")

if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

for item in sorted(item_dict):
    if item_dict[item]["crafted"] > 0:
        print(f"{item}: {item_dict[item]['crafted']}")
    else:
        pass