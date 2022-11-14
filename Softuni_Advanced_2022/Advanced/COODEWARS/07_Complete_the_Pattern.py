def pattern(n):
    lst = []
    if n < 1:
        return ""
    for i in range(n + 1):
        member = str(i) * int(i)
        lst.append(member)

    return lst[0] + "\n".join(lst[1::])


n = int(input())
print(pattern(n))