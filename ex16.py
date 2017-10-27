from sys import argv

script, file_name = argv
print(f"we are going to erase file {file_name}.")
print("If you dont want that, hit Ctrl+c (^c).")
print("Hit enter to continue.")
input('?')
print("Opening the file...")
target = open(file_name,'w')
# print(target.read())
print("truncating the file. Gud bye!")
target.truncate()

print("now im going to ask you for three lines")
line1 = input("line1 is :")
line2 = input("line2 is :")
line3 = input("line3 is :")

print(f"I am going to write these to file {file_name}")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally we close it")
target.close()
