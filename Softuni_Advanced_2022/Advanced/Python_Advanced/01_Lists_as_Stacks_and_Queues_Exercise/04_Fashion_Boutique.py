clothes_sizes = input()
rack_size = int(input())
rack_counter = 1
list_clothes_sizes = list(map(int, clothes_sizes.split()))
rack = rack_size

for i in range(len(list_clothes_sizes) - 1, 0 - 1, -1):

    rack -= list_clothes_sizes[i]
    if rack >= 0:
        pass
    else:
        rack = rack_size
        rack -= list_clothes_sizes[i]
        rack_counter += 1

print(rack_counter)