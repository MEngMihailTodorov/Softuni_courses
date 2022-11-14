lst = input().split("|")

sub_lst = []

for sub_string in lst[::-1]:
    sub_lst.extend(sub_string.split())

print(*sub_lst)