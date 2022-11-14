def reverse_numbers(n):
    str_list = list(map(str, n.split()))
    return " ".join(str_list[-i] for i in range(1, len(str_list) + 1))


n = input()
print(reverse_numbers(n))