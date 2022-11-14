# count = 0
#
# for i in range(8):  # 0, 1, 2, 3, 4, 5, 6, 7
#     for j in range(3):  # 0, 1, 2
#         print(i, j)
#         count += 1
#
# print(count)

command = ['Greece', '1000', '200', '200', '300', '100', '150', '240', "Spain", '1200', '300', '500', '193', '423', 'End']
index = 0

while command[index] != 'End':
    current_destination = command[index]
    index += 1
    current_destination_price = int(command[index]) # Number(command[index])
    index += 1
    current_available_sum = 0

    while command[index].isdigit():
        current_available_sum += int(command[index])
        index += 1

    if current_available_sum >= current_destination_price:
        print(f"You are going to {current_destination}")
    else:
        print(f"You are not going to {current_destination}")
