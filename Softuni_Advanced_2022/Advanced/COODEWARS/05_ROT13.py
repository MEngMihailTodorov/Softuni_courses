def rot13(message):
    cypher = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                char = (ord(char) + 13)
                if char > 122:
                    char = chr(char - 26)
                else:
                    char = chr(char)
            elif char.isupper():
                char = (ord(char) + 13)
                if char > 90:
                    char = chr(char - 26)
                else:
                    char = chr(char)
            cypher += char
        else:
            cypher += char

    return cypher


message = input()
print(rot13(message))