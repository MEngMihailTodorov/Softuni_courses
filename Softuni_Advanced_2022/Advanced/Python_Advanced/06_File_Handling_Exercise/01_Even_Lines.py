import os

symbols = ["-", ",", ".", "!", "?"]

file_path = 'resources/text.txt'

try:
    with open(file_path, 'r') as even_lines_file:
        text = even_lines_file.readlines()

    for row in range(0, len(text), 2):
        for symbol in symbols:
            text[row] = text[row].replace(symbol, "@")

        print(*text[row].split()[::-1], sep=" ")

except FileNotFoundError:
    print(f"File does not exist or was not found!")

