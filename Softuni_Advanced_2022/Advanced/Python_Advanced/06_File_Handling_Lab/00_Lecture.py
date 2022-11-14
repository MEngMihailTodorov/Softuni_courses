from os import path

# file = open('./misho.txt')
file2 = open('./resources/misho_2', 'r')
file_path1 = "./resources/misho_2"
file = open(file_path1)

print(file)
print(file2)
print(path.abspath(file_path1))