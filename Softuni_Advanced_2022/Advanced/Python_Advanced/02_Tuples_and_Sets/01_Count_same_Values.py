def number_counter(n):
    lst = list(map(float, n.split()))
    my_dict = {}

    for i in lst:
        if i in my_dict.keys():
            my_dict[i] += 1
        else:
            d = {i: 1}
            my_dict.update(d)

    return "\n".join(f"{key} - {my_dict[key]} times" for key in my_dict.keys())


n = input()
print(number_counter(n))