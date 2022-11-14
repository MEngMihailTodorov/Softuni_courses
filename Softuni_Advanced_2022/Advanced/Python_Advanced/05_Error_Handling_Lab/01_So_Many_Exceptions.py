numbers_list = list(map(int, input().split(", ")))
result = 1
length = len(numbers_list)

for i in range(length):
    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result)


















