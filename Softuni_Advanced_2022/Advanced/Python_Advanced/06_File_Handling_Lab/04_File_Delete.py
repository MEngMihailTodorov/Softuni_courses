from os import remove
from os import linesep
from os import listdir
from os import path

# file_path = "./output.txt"
#
# with open(file_path, 'r+') as file:
#     original_content = file.read()
#     new_content = "placeholder text" + original_content
#     file.seek(0)
#     file.truncate(0)
#     file.write(new_content)

try:
    remove('./my_first_file.txt')
    print(listdir('./'))
    print("File removed!")
except FileNotFoundError:
    print(f"File does not exist!")
    print(listdir('./'))

