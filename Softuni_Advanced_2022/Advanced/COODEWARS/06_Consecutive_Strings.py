def longest_consec(strarr, k):
    if len(strarr) == 0:
        return ""
    longest_string = ""
    for i in strarr:
        current_string = "".join(str(strarr[j]) for j in range(i, i + int(k) + 1))
        if len(current_string) > len(longest_string):
            longest_string = current_string

    return longest_string


strarr = input().split()
k = int(input())
print(longest_consec(strarr, k))