file_path = r"./numbers.txt"

file = open(file_path, 'r')

result = 0

for line in file:
    result += int(line[0])

print(result)