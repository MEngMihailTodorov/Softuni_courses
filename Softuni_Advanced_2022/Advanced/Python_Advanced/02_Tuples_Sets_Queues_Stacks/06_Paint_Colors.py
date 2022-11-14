from collections import deque

main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]

main_color_collection = []
secondary_color_collection = []
string_list = deque(map(str, input().split()))

while string_list:
    if len(string_list) > 1:
        str_1 = string_list[0]
        str_2 = string_list[-1]

        if str_1 + str_2 in main_colors:
            main_color_collection.append(str_1 + str_2)
            string_list.popleft()
            string_list.pop()

        elif str_2 + str_1 in main_colors:
            main_color_collection.append(str_2 + str_1)
            string_list.popleft()
            string_list.pop()

        elif str_2 + str_1 in secondary_colors:
            secondary_color_collection.append(str_2 + str_1)
            main_color_collection.append(str_2 + str_1)
            string_list.popleft()
            string_list.pop()

        elif str_1 + str_2 in secondary_colors:
            secondary_color_collection.append(str_1 + str_2)
            main_color_collection.append(str_1 + str_2)
            string_list.popleft()
            string_list.pop()

        else:
            first_stripped, second_stripped = str_1[:-1], str_2[:-1]
            string_list.popleft()
            string_list.pop()
            if first_stripped:
                string_list.insert(len(string_list) // 2, first_stripped)
            if second_stripped:
                string_list.insert(len(string_list) // 2, second_stripped)

    else:

        substring = string_list.popleft()
        if substring in main_colors:
            main_color_collection.append(substring)
        elif substring in secondary_color_collection:
            secondary_color_collection.append(substring)
        else:
            pass

secondary_color_collection = main_color_collection.copy()

red = False
blue = False
yellow = False

for i in main_color_collection:
    if i == "red":
        red = True
    elif i == "blue":
        blue = True
    elif i == "yellow":
        yellow = True


for j in secondary_color_collection:
    if j == "orange":
        if red and yellow:
            pass
        else:
            secondary_color_collection.remove("orange")
    if j == "purple":
        if red and blue:
            pass
        else:
            secondary_color_collection.remove("purple")
    if j == "green":
        if blue and yellow:
            pass
        else:
            secondary_color_collection.remove("green")

print(secondary_color_collection)