from sys import argv

script, file_name = argv

# print("the comman line arguments of this program is {}, {} {}".format(*argv))

text = open(file_name)
text.close()

print(text.read())
