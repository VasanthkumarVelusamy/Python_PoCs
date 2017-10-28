from sys import argv

file_name = argv[1]

def print_all(f):
    print(">>>>>>>Print all: f is :",f)
    print(f.read())
    print(">>>>>>>Print all: f is :",f)

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(">>>>>>>Print a line: f is :",f)
    print(line_count, f.readline(), end='')
    print(">>>>>>>Print a line: f is :",f)

current_file = open(file_name)

# lets print all the data in the file
print("lets print all the data in the file")

print_all(current_file)

# lets rewind to top of the file
print("lets rewind to top of the file")

rewind(current_file)

# so now lets print line by line
print("so now lets print line by line")

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line +1
print_a_line(current_line,current_file)

current_file.close()
