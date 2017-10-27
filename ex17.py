from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"copying the file from {from_file} to {to_file}")
in_data = open(from_file).read()

print(f"the input file is {len(in_data)} bytes long")
print(f"does the output file exist? {exists(to_file)}")
input("Hit enter to continue or press Ctrl+c to abort: ")

outfile = open(to_file,'w')
outfile.write(in_data)
outfile.write("vasanth\n")

print("Alright, all done!")
outfile.close()
