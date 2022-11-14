file_path = './text.txt'


try:
    file = open(file_path, 'r')
    print(file.readline())
    print("File found.")

except FileNotFoundError:
    print(f"File not found")