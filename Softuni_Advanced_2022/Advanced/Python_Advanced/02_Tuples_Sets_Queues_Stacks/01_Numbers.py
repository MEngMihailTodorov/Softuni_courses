first_num = set(map(int, input().split()))
second_num = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    command = input()
    if "Add First" in command:
        for i in command.split()[2::]:
            first_num.add(int(i))
    elif "Add Second" in command:
        for i in command.split()[2::]:
            second_num.add(int(i))
    elif "Remove First" in command:
        for i in command.split()[2::]:
            first_num.discard(int(i))
    elif "Remove Second" in command:
        for i in command.split()[2::]:
            second_num.discard(int(i))
    else:
        print(True if first_num.issubset(second_num) or second_num.issubset(first_num) else False)

print(", ".join(str(j) for j in sorted(first_num)))
print(", ".join(str(j) for j in sorted(second_num)))