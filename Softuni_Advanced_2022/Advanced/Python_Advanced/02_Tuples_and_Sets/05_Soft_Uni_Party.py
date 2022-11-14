n = int(input())
regular = []
vip = []

for i in range(n):
    code = input()
    if code[0].isdigit():
        vip.append(code)
    else:
        regular.append(code)

while True:
    new_code = input()

    if new_code == "END":
        break

    if new_code[0].isdigit():
        vip.remove(new_code)
    else:
        regular.remove(new_code)

regular = sorted(regular)
vip = sorted(vip)

print(f"{(len(regular) + len(vip))}")
for j in vip:
    print(j)
for k in regular:
    print(k)