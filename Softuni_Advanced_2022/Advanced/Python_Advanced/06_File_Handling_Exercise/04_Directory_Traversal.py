import os

directory = input()

extensions_dict = {}

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)

    if os.path.isfile(file):
        extension = filename.split(".")[-1]

        if extension not in extensions_dict:
            extensions_dict[extension] = []
        extensions_dict[extension].append(str(filename))


print(extensions_dict)
extensions_dict = sorted(extensions_dict.items(), key=lambda x: (x[0]))
print(extensions_dict)

for key in extensions_dict:
    print(f".{key[0]}")
    for key_file in key[1]:
            print(f"- - - {key_file}")
