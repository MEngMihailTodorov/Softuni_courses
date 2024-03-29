def palindrome(word: str, index: int):
    if index == len(word) // 2:
        return f"{word} is a palindrome"
    if word[index] == word[-index-1]:
        index += 1
        return palindrome(word, index)
    elif word[index] != word[-index - 1]:
        return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))