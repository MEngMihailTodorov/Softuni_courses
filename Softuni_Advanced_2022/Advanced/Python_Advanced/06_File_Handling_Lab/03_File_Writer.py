from os import linesep
#
# file_path = "./output.txt"
#
# file = open(file_path, 'w')
# file.write("hello world!" + linesep)
# file.write("hello world!" + linesep)
# file.write("hello world!" + linesep)

file_path = './my_first_file.txt'

with open(file_path, 'w') as file:
    file.write("I just created my nth file in python!" + linesep)