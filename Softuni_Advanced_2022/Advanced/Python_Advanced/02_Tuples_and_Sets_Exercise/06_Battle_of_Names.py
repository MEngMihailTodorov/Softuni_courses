n = int(input())
current_low = 1
odd_set = set()
even_set = set()

for i in range(n):
    name = input()
    name_sum = 0
    for char in name:
        name_sum += int(ord(char))

    name_sum = name_sum / current_low
    current_low += 1
    if int(name_sum) % 2 == 0:
        even_set.add(int(name_sum))
    elif int(name_sum) % 2 == 1:
        odd_set.add(int(name_sum))

if sum(odd_set) == sum(even_set):
    result = odd_set | even_set

elif sum(odd_set) < sum(even_set):
    result = odd_set ^ even_set
elif sum(odd_set) > sum(even_set):

    result = odd_set - even_set

print(", ".join(str(i) for i in result))

