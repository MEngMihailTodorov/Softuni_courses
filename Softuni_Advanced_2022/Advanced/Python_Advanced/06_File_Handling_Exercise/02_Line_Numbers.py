from string import punctuation

try:
    output_file = open("resources/output.txt", "a")

    with open("resources/text.txt", 'r') as text_file:
        text = text_file.readlines()

    for i in range(len(text)):
        row = text[i]

        letters = 0
        marks = 0

        for symbol in row:
            if symbol.isalpha():
                letters += 1
            elif symbol in punctuation:
                marks += 1

        output_file.write(f"Line {i + 1}: {''.join(row.strip())} ({(letters)}) ({(marks)})" + '\n')

except FileNotFoundError:
    print(f"File with specified name does not exists!")